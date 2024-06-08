const SCRIPT_ROOT = 'http://127.0.0.1:5000';

let liToEdit = null;


function createItem(itemValue, id) {
    let li = document.createElement("li");
    li.className = "list-group-item";
    li.id = id;

    let deleteButton = document.createElement("button");

    deleteButton.className =
        "btn-danger btn btn-sm float-right delete";

    deleteButton.appendChild(document.createTextNode("Delete"));
    deleteButton.onclick = function() {
        this.parentNode.parentNode.removeChild(li);

        const delete_task_url = SCRIPT_ROOT + '/delete/' + this.parentNode.id;
        fetch(delete_task_url, {
            "method": "GET",
        }).then((response) => {
            console.log(response);
        });
    }

    let editButton = document.createElement("button");
    editButton.onclick = function() {
        const box = document.getElementById("box");
        box.value = this.parentNode.firstChild.nodeValue;
        liToEdit = {id: this.parentNode.id, name: this.parentNode.firstChild.nodeValue};
        this.parentNode.parentNode.removeChild(li);
    }

    editButton.className =
        "btn-success btn btn-sm float-right edit";

    editButton.appendChild(document.createTextNode("Edit"));

    li.appendChild(document.createTextNode(itemValue));
    li.appendChild(deleteButton);
    li.appendChild(editButton);

    return li;
}

// Function called while clicking add button
function add_item() {
    console.log(SCRIPT_ROOT);
    // Getting box and ul by selecting id;
    let box = document.getElementById("box");
    let list_item = document.getElementById("list_item");
    if (box.value != "") {
        let url = '';
        if (liToEdit == null) {
            url = SCRIPT_ROOT + '/add';
        }  else {
            url = SCRIPT_ROOT + '/modify/' + liToEdit.id;
            liToEdit = null;
        }

        let data = new FormData()
        data.append("name",box.value)
        fetch(url, {
            "method": "POST",
            "body": data,
        }).then((response) => {
            return response.json();
        }).then((resp) => {
            console.log(resp);
            const li = createItem(box.value, resp.id);
            list_item.appendChild(li);
            box.value = "";
        });
    }
    else {

        // Alert msg when value of box is "" empty.
        alert("Add value to item");
    }

}

function fetchTasks() {
    const add_task_url = SCRIPT_ROOT + '/task';
    fetch(add_task_url, {
        "method": "GET",
    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
        const list_item = document.getElementById("list_item");
        for (let i = 0; i < data.length; i++) {
            const li = createItem(data[i].name, data[i].id);
            list_item.appendChild(li);
        }
    });
}


