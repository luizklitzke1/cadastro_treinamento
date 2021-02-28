//Script para declaração e controle da validação dos forumários em tempo real

//Variável que garante que todos os campos sejam válidos 
var formValid = {
    cpf: false,
    nome : false,
    sobrenome : false,
};


//Verifica se todos os campos estão válidos
function checkFormPessoa(){
    var check = true;

    $.each(formValid, function(index, element) {
        if (!element){
            check = false;
        };
    });
    if ($("#selectSala1").val() == null){
        check = false;
    }
        
    if ($("#selectCafe1").val()  == null){
        check = false;
    }
    if ($("#selectCafe2").val()  == null){
        check = false;
    }	


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
var testeLetters2 = new RegExp(/^[\s\d\p{L}]*$/ui);

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
    checkFormPessoa();
    
});


//Verificação customizada do nome
$("#campoNome").on('input', function() {
    var input= $(this);

    if (input.val().length <3){
        msg("#inv-nome","O nome deve ter no mínimo 3 caracteres!");
        formValid["nome"] = false;
    }
    else {
        if (testeLetters2.test(input.val())){
            formValid["nome"] = true;
        }
        else{
            msg("#inv-nome","O nome deve conter apenas letras ou números!");
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
    checkFormPessoa();
    
});

//Verificação customizada do sobrenome
$("#campoSobrenome").on('input', function() {
    var input= $(this); 
    if (input.val().length <3){
        msg("#inv-sobrenome","O sobrenome deve ter no mínimo 3 caracteres!");
        formValid["sobrenome"] = false;
    }
    else {
        if (testeLetters2.test(input.val())){
            formValid["sobrenome"] = true;
        }
        else{
            msg("#inv-sobrenome","O sobrenome deve conter apenas letras ou números!");
            formValid["sobrenome"] = false;
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
    checkFormPessoa();
    
});


function validarCPF(cpf) {	
    
    cpf = String(cpf).replace(/[^\d]+/g,'');	
    if(cpf == '') return false;	
    // Elimina CPFs invalidos conhecidos	
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

//Variável que garante que todos os campos sejam válidos 
var formValid2 = {
    cpf: true,
    nome : true,
    sobrenome : true,
};

    
//Verifica se todos os campos estão válidos
function checkFormPessoa2(){
    var check = true;

    for(var key in formValid2){
        if (!(formValid2[key])){
            check = false;
        }
    }


    //Fora do loop para evitar problemas com sync 
    if (check){
        $('#btnEditarPessoa').removeAttr('disabled');
        return true;
    }
    else{
        $('#btnEditarPessoa').attr('disabled', true);
        return false;
    }
    
    };

//Verificação customizada do nome
$("#campoCPFPessoaEditar").on('input', function() {
    var input= $(this);

    if (!validarCPF(input.val())){
        msg("#inv_cpf_pessoa_editar","CPF inválido");
        formValid2["cpf"] = false;
    }
    else {
        formValid2["cpf"] = true;
    }   

    if (formValid2["cpf"]){
        $("#inv_cpf_pessoa_editar").hide();
        input.removeClass("invalid").addClass("valid");
    }
    else{
        show("#inv_cpf_pessoa_editar");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkFormPessoa2();
    
});


//Verificação customizada do nome
$("#campoNomePessoaEditar").on('input', function() {
    var input= $(this);

    if (input.val().length <3){
        msg("#inv_nome_pessoa_editar","O nome deve ter no mínimo 3 caracteres!");
        formValid2["nome"] = false;
    }
    else {
        if (testeLetters2.test(input.val())){
            formValid2["nome"] = true;
        }
        else{
            msg("#inv_nome_pessoa_editar","O nome deve conter apenas letras ou números!");
            formValid2["nome"] = false;
        };
    }   

    if (formValid2["nome"]){
        $("#inv_nome_pessoa_editar").hide();
        input.removeClass("invalid").addClass("valid");
    }
    else{
        show("#inv_nome_pessoa_editar");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkFormPessoa2();
    
});

//Verificação customizada do sobrenome
$("#campoSobrenomePessoaEditar").on('input', function() {
    var input= $(this); 
    if (input.val().length <3){
        msg("#inv_sobrenome_pessoa_editar","O sobrenome deve ter no mínimo 3 caracteres!");
        formValid2["sobrenome"] = false;
    }
    else {
        if (testeLetters2.test(input.val())){
            formValid2["sobrenome"] = true;
        }
        else{
            msg("#inv_sobrenome_pessoa_editar","O sobrenome deve conter apenas letras ou números!");
            formValid2["sobrenome"] = false;
        };
    }   

    if (formValid2["sobrenome"]){
        $("#inv_sobrenome_pessoa_editar").hide();
        input.removeClass("invalid").addClass("valid");

    }
    else{
        show("#inv_sobrenome_pessoa_editar");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkFormPessoa2();
    
});

$('#selectCafe1').on('change', function (e) {
    var optionSelected = $("option:selected", this);
    var valueSelected = this.value;
    //Pegar as opções de espaço de café
    $.ajax({
        url: "http://localhost:5000/listar_espacos_cafe",
        method: "GET",
        dataType: "json", 
        success: listaresp, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listaresp (espacos) {
        // Limpa os dados da tabela
        $("#selectCafe2").empty();    
        
        // Percorre todas os espaços registradas
        for (espaco of espacos){

            if (espaco.id_espaco != valueSelected){
                // Cria uma nova linha para cada espaço
                op =
                "<option value= '" + espaco.id_espaco+"'>"+ espaco.nome + "</option>"

                    // Adiciona a nova linha na tabela
                    $("#selectCafe2").append(op);
            }
          
        }
        checkFormPessoa();
        
    }
    
  
});