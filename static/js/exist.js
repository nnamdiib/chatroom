function login(room, nick){
    var h;
    h = window.location.host  + '/chat.html/?room=' + room + '&nick=' + nick;
    window.location = '/?room=' + room + '&nick=' + nick;
}

function update_send() {
    if ( $("#txtNickname").val() != "" && $("input[name = 'room']:checked").val() != "") {
    	room = $("input[name = 'room']:checked").val();
		nick = $('#txtNickname').val();
		login(room, nick)
            
    }
            
};