var ppnId = "ppn-aWNvb2s=-0";
var tw = window.top, sfe = window.frameElement;
var container = document.createElement('div');
container.id = ppnId;

var closeButton = document.createElement('span');
closeButton.innerText = "x";
closeButton.setAttribute("style", "background: #ccc;float: right;width: 20px;height: 20px;text-align: center;line-height: 17px;font-size: 20px;");

closeButton.addEventListener('click', function (event) {
    closeButton.style.display = "none";
    container.style.display = "none";
});
sfe.parentNode.insertBefore(closeButton,sfe);
sfe.parentNode.insertBefore(container, sfe);

if(tw.ppnio){
    tw.ppnio.push(ppnId);
}else{
    tw.ppnio = [ppnId];
    var ppnioScript = document.createElement('script');
    ppnioScript.type = 'text/javascript';
    ppnioScript.src = 'https://player.svc.litv.tv/v3/ppnio.js';
    tw.document.body.appendChild(ppnioScript);
}