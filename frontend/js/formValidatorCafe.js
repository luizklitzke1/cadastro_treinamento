//Script para declaração e controle da validação dos forumários de salas e espaços de facé em tempo real
// Separado do padrão de HTML para melhor customização e controle

//Variável que garante que todos os campos sejam válidos 
var formValid = {
    nome : false,
};


//Verifica se todos os campos estão válidos
function checkFormCafe(){

    var check = true;
    
    if (!formValid.nome){
        check = false;
    };

    //Fora do loop para evitar problemas com sync 
    if (check){
        $('#btnAdCafe').removeAttr('disabled');
        return true;
    }
    else{
        $('#btnAdCafe').attr('disabled', true);
        return false;
    }
    
    };

//Muda a mensagem de erro nos inputs
function msg(id,message){
    $(id).text(message).show;
}

//Mostra a div com a msg
function show(id){
    $(id).show();
}

//Padrão de verificação dos caracteres de texto
//var textEsp = new RegExp(/^[a-zA-Z0-9]+$/);

//Verificação customizada do nome
var testeLetters3 = new RegExp(/^[\s\d\p{L}]*$/ui);

$("#campoNomeCafe").on('input', function() {
    var input= $(this);

    if (input.val().length <3){
        msg("#inv-nome-cafe","O nome deve ter no mínimo 3 caracteres!");
        formValid["nome"] = false;
    }
    else {
        if (testeLetters3.test(input.val())){
            formValid["nome"] = true;
        }
        else{
            msg("#inv-nome-cafe","O nome deve conter apenas letras ou números!");
            formValid["nome"] = false;
        };
    }   

    if (formValid["nome"]){
        $("#inv-nome-cafe").hide();
        input.removeClass("invalid").addClass("valid");
    }
    else{
        show("#inv-nome-cafe");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkFormCafe();
    
});

//Verifica se todos os campos estão válidos
function checkFormCafe2(){

    var check = true;
    
    if (!formValid.nome){
        check = false;
    };

    //Fora do loop para evitar problemas com sync 
    if (check){
        $('#btnEditarCafe').removeAttr('disabled');
        return true;
    }
    else{
        $('#btnEditarCafe').attr('disabled', true);
        return false;
    }
    
    };


$("#campoNomeCafeEditar").on('input', function() {
    var input= $(this);

    if (input.val().length <3){
        msg("#inv-nome-cafe-editar","O nome deve ter no mínimo 3 caracteres!");
        formValid["nome"] = false;
    }
    else {
        if (testeLetters3.test(input.val())){
            formValid["nome"] = true;
        }
        else{
            msg("#inv-nome-cafe-editar","O nome deve conter apenas letras ou números!");
            formValid["nome"] = false;
        };
    }   

    if (formValid["nome"]){
        $("#inv-nome-cafe-editar").hide();
        input.removeClass("invalid").addClass("valid");
    }
    else{
        show("#inv-nome-cafe-editar");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkFormCafe2();
    
});




