//Script para declaração e controle da validação dos forumários em tempo real

//Variável que garante que todos os campos sejam válidos 
var formValid = {
    cpf: false,
    nome : false,
    sobrenome : false,
};

    
//Torna todos os valores válidos caso estiver apenas editando
if ($("#form_editar").length){
    formValid = { 
        cpf: false,
        nome : false,
        sobrenome : false,
    };
    checkForm();
}

//Verifica se todos os campos estão válidos
function checkForm(){

    var check = true;

    $.each(formValid, function(index, element) {
        if (!element){
            check = false;
        };
    });

    //Fora do loop para evitar problemas com sync 
    if (check){
        $('#btnAdPessoa').removeAttr('disabled');
        return true;
    }
    else{
        $('#btnAdPessoa').attr('disabled', true);
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
var testeLetters = new RegExp(/^[\s\p{L}]*$/ui);

//Verificação customizada do nome
$("#campoCPF").on('input', function() {
    var input= $(this);

    if (!validarCPF(input.val())){
        msg("#inv-cpf","CPF inválido");
        formValid["cpf"] = false;
    }
    else {
        formValid["cpf"] = true;
    }   

    if (formValid["cpf"]){
        $("#inv-cpf").hide();
        input.removeClass("invalid").addClass("valid");
    }
    else{
        show("#inv-cpf");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkForm();
    
});


//Verificação customizada do nome
$("#campoNome").on('input', function() {
    var input= $(this);
    console.log(testeLetters.test(input.val()));

    if (input.val().length <3){
        msg("#inv-nome","O nome deve ter no mínimo 3 caracteres!");
        formValid["nome"] = false;
    }
    else {
        if (testeLetters.test(input.val())){
            formValid["nome"] = true;
        }
        else{
            msg("#inv-nome","O nome deve conter apenas letras!");
            formValid["nome"] = false;
        };
    }   

    if (formValid["nome"]){
        $("#inv-nome").hide();
        input.removeClass("invalid").addClass("valid");
    }
    else{
        show("#inv-nome");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkForm();
    
});

//Verificação customizada do sobrenome
$("#campoSobrenome").on('input', function() {
    var input= $(this); 
    if (input.val().length <3){
        msg("#inv-sobrenome","O sobrenome deve ter no mínimo 3 caracteres!");
        formValid["sobrenome"] = false;
    }
    else {
        if (testeLetters.test(input.val())){
            formValid["nome"] = true;
        }
        else{
            msg("#inv-nome","O nome deve conter apenas letras!");
            formValid["nome"] = false;
        };
    }   

    if (formValid["sobrenome"]){
        $("#inv-sobrenome").hide();
        input.removeClass("invalid").addClass("valid");

    }
    else{
        show("#inv-sobrenome");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkForm();
    
});


function validarCPF(cpf) {	
    
    cpf = String(cpf).replace(/[^\d]+/g,'');	
    if(cpf == '') return false;	
    // Elimina CPFs invalidos conhecidos
    console.log(cpf);	
    if (cpf.length != 11 || 
        cpf == "00000000000" || 
        cpf == "11111111111" || 
        cpf == "22222222222" || 
        cpf == "33333333333" || 
        cpf == "44444444444" || 
        cpf == "55555555555" || 
        cpf == "66666666666" || 
        cpf == "77777777777" || 
        cpf == "88888888888" || 
        cpf == "99999999999")
            return false;		
    // Valida 1o digito	
    add = 0;	
    for (i=0; i < 9; i ++)		
        add += parseInt(cpf.charAt(i)) * (10 - i);	
        rev = 11 - (add % 11);	
        if (rev == 10 || rev == 11)		
            rev = 0;	
        if (rev != parseInt(cpf.charAt(9)))		
            return false;		
    // Valida 2o digito	
    add = 0;	
    for (i = 0; i < 10; i ++)		
        add += parseInt(cpf.charAt(i)) * (11 - i);	
    rev = 11 - (add % 11);	
    if (rev == 10 || rev == 11)	
        rev = 0;	
    if (rev != parseInt(cpf.charAt(10)))
        return false;		
    return true;   
}

//Padrão de verificação dos caracteres de texto para o resumo
//Desativado por problemas com UTF-8
//var textEspHist = new RegExp(/^[\p{L}a-zA-Z0-9-!?"'/,. ]+$/);


