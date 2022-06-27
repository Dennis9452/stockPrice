

(function(){ 
    var sesStorage = JSON.parse(sessionStorage.getItem("player"));
    var select = document.getElementById("player");
    var playerList = [];
    var nowRoster = {};

    var addButton;
    var removeButton;

    (function(){ if(!sesStorage) {
        getPlayer().then(function(response){
            console.log(response)
            var res = JSON.parse(response)
            appendSelection(res);
        })
    }else{
        appendSelection(sesStorage);
    }}())


    function appendSelection(data){
        addSelection(data.player);
        sessionStorage.setItem("player", JSON.stringify(data));
        bindingListener();
    }

    function bindingListener(){
        addButton = document.getElementById("add");
        removeButton = document.getElementById("remove"); 
        sendButton = document.getElementById("send"); 

        addButton.addEventListener("click", playerModification);
        removeButton.addEventListener("click", playerModification);
        sendButton.addEventListener("click", searchStats);
    }

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
            xhr.open("GET", "https://127.0.0.1:5000/getPlayer");
            
            xhr.send();
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        console.log(xhr);
                        resolve(xhr.response);
                    } else {
                        reject(new Error(xhr.statusText));
                    }
                }
            }

            xhr.onerror = function() {
                console.log("onerror");
                reject(new Error('Network Error'))
            }
        })
    }

    function isDuplicate(value){
        if(nowRoster[value] == 1) return true;
        else return false;
    }

    function modificationNotice(data, action){
        var notice = document.getElementById("notice");
        switch(action){
            case "duplicated":
                notice.innerText = data + " is duplicated";
                break;
            case "add":
                notice.innerText = data + " has added";
                break;
            case "remove":
                notice.innerText = data + " has remove";
                break;
        }
    }


    function playerModification(e){
        var temp = document.getElementById("playerSelected");
        var playerName = select.value;
        if(e.target == addButton){
            if(isDuplicate(playerName)) {
                modificationNotice(playerName, "duplicated");
                return;
            }
            temp.innerText += playerName + ",";
            playerList.push(playerName);
            nowRoster[playerName] = 1;
            modificationNotice(playerName, "add");
        }else{
            temp = playerSelected.childNodes;
            playerList.pop();
            nowRoster[playerName] = 0;
            playerSelected.removeChild(temp[temp.length-1]);
            modificationNotice(playerName, "remove");
        }
    }

    function searchStats(){
        return new Promise(function(resolve, reject) {
            xhr = new XMLHttpRequest();
            xhr.open("POST", "https://127.0.0.1:5000/getStats");
            xhr.setRequestHeader("Content-Type", "application/json");
            console.log(playerList)
            xhr.send( JSON.stringify({"player" : playerList} ));
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        searchResult(JSON.parse(xhr.response));
                        resolve();
                    } else {
                        reject(new Error(xhr.statusText));
                    }
                }
            }
            
            xhr.onerror = function() {
                reject(new Error('Network Error'))
            }
        });
    }

    function searchResult(data){
        var table = document.getElementById('myTable')
        var tbodyRef = table.getElementsByTagName('tbody')[0];
        
        var result = data.result;
        for(player in playerList){
            var newRow = tbodyRef.insertRow();
            var newCell = newRow.insertCell();
            var newText = document.createTextNode(playerList[player]);
            newCell.appendChild(newText);
            for(stats in result[player]){
                var text = result[player][stats];
                var newCell = newRow.insertCell();
                var newText = document.createTextNode(text);
                newCell.appendChild(newText);
            }
        }
        table.style.display = "block";
    }

}())