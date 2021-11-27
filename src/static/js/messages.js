let loc = window.location;
let wsStart = 'wss://';

// if(loc.protocol === 'https'){
//     wsStart = 'wss://'
// }

let ept = wsStart + loc.host;

var socket = new WebSocket("wss://localhost:");

socket.onopen = async function(e){
    console.log('open', e);
}

socket.onmessage = async function(e){
    console.log('message', e);
}

socket.onerror = async function(e){
    console.log('error aya bhiya', e);
}

socket.onclose = async function(e){
    console.log('close', e);
}