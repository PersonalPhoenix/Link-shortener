function validation(form){

    function removeError(input){
        const parent = input.parentNode;

        if(parent.classList.contains('error')){
            parent.querySelector('.error-label').remove()
            parent.classList.remove('error')
        }
    }

    function createError(input, text){
        const parent = input.parentNode;
        const errorLabel = document.createElement('label')
        errorLabel.classList.add('error-label')
        errorLabel.textContent = text
        parent.classList.add('error')
        parent.append(errorLabel)
    }

    const allInputs = form.querySelectorAll('input');
    let result = true;

    

    for (const input of allInputs){
        removeError(input)
        if (input.value==''){
            createError(input, 'Поле не заполнено')
            result = false
        }
    }
    return result
}



// $(document).on('submit', '#post-form', function(event){
//document.getElementById('#post-form').addEventListener('submit', function(event){
$(document).on('submit', '#post-form', function(event){
    event.preventDefault();
    if(validation(this) == true){
        $.ajax({
            type: 'POST',
            url: '/create',
            data:{
                link:$('#link').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data){
            $('#section>h2').html('localhost:8000/'+data)
            }
        })
    }
})
