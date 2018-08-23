$(document).ready(function(){
$('#add').click(function(e){
event.preventDefault()
$('#items').append( '<div><input type="text" name="amount">'
                    +'<input type="text" name="service">'
                    +'<input type="text" name="value" >'
                    +'<input type="text" name="total">'
                    +'<input type="button" name="delete" id="delete"></div>')
});
$('body').on('click','#delete',function(e){
    $(this).parent('div').remove();
})
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


function sure(cas) {
    var txt;
    var r = confirm("Desea eliminar la información!");
    if (r == true) {
        if(cas===1){
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open( "GET", "/delete");
            window.replace("/");
        }
        if(cas===2){

        }
        if(cas===3){

        }                
    } else {
        
    }

}