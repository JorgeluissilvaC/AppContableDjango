function sure(id) {
    let cas = document.getElementById(id).name;
    var params = "IDD="+id+"&tipo="+cas+"";
    var r = confirm("Desea eliminar la información!");
    if (r == true) {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open( "GET", "/delete/?"+params);
            xmlHttp.send( null );
            alert("Información eliminada!");  
    }else{
        alert("La información no fue eliminada");
    }
}


$(document).ready(function(){
    $('#add').click(function(e){
    var s = new String;
    var arr = new Array;
    s = $('#id_service').val()+"";
    arr = s.split(" ")
    event.preventDefault();
    $('#items').append( '<div><input type="text" name="amount">'
                        +'<input type="text" name="" value="'+arr[1].replace(',','.').replace(' ',' ')+'">'
                        +'<input type="text" name="value" value="'+ arr[2].replace(',','.').replace(' ','')+'">'
                        +'<input type="text" name="total" value="'+ Number(arr[1].replace(',','.'.replace(' ','')))*Number(arr[2].replace(',','.').replace(' ',''))+'">'
                        +'<button id="delete"> Borrar </button></div>')
    });
    $('body').on('click','#delete',function(e){
        $(this).parent('div').remove();
    })
    //Selector
    $('#custome').hide();
    $('#technicia').hide();
    $('#service').hide();
    
        $('#customer').click(function(){
            $('#custome').show();
            $('#technicia').hide();
            $('#service').hide();
    
        });
        $('#technician').click(function(){
            $('#custome').hide();
            $('#technicia').show();
            $('#service').hide();
    
        });
        $('#services').click(function(){
            $('#custome').hide();
            $('#technicia').hide();
            $('#service').show();
    
        });
    });
    