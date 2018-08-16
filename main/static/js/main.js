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
});