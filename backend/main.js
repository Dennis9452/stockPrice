var playerList = [];
var select = document.getElementById("player");
var addButton = document.getElementById("add");
var removeButton = document.getElementById("remove");

(function(){ 
    var sesStorage = sessionStorage.getItem("player")  
    console.log(sesStorage);
    if(!sesStorage) {
        getPlayer().then(function(response){
            var res = JSON.parse(response)
            addSelection(res.player);
            sessionStorage.setItem("player",response);
        })
    }else{
        addSelection(sesStorage.player);
    }

    addButton.addEventListener("click", playerModification);
    removeButton.addEventListener("click", playerModification);
}())

function addSelection(list){
    for( i in list){
        var opt = document.createElement('option');
        opt.value = list[i];
        opt.innerHTML = list[i];
        select.appendChild(opt);
    }
}

function getPlayer(){
    return new Promise(function(resolve, reject) {
        xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/getPlayer");
        
        xhr.send();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    resolve(xhr.response);
                } else {
                    reject(new Error(xhr.statusText));
                }
            }
        }
        
        xhr.onerror = function() {
            reject(new Error('Network Error'))
        }
    })
}


function playerModification(e){
    console.log(e);
    var temp;
    if(e.target == addButton){
        temp = document.createElement("p");
        temp.innerText = select.value
        playerSelected.appendChild(temp);
    }else{
        temp = playerSelected.childNodes;
        playerSelected.removeChild(temp[temp.length-1]);
    }
}

