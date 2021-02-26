//Registrar nova sala
function cadastrarSala ()  {

    nome = $("#campoNomeSala").val();

    var dados = JSON.stringify({nome: nome});

    // Enivo dos dados ao back-end para a inclusão
    $.ajax({
        url: 'http://localhost:5000/cadastrar_sala',
        type: 'POST',
        dataType: 'json', contentType: 'application/json',
        data: dados, 
        success: salaIncluida, 
        error: erroAoIncluir

    });
    function salaIncluida (retorno) {
        if (retorno.resultado == "ok") { 
            alert("Sala " + nome + " registrada com sucesso!");
            // Limpar o campo
            $("#campoNome").val("");
            popularSalasGeral();

        } 
        else {
            // informar mensagem de erro
            alert(retorno.resultado + ":" + retorno.detalhes);
        };            
    };
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        };
};

//Apagar sala baseado no ID
function apagarSala(id_sala){
    $.ajax({
        url: 'http://localhost:5000/apagar_sala/'+id_sala,
        type: 'DELETE',
        dataType: 'json', contentType: 'application/json',
        data: JSON.stringify({ id_sala: id_sala}), 
        success: function(retorno){
            if (retorno.resultado == "ok") {
                $("#trSala_" + id_sala).fadeOut(600, function(){ 
                alert("Sala apagada com sucesso!"); 
                popularSalasGeral();
                
            });
            
        }
            else {
                alert(retorno.resultado + " : " + retorno.detalhes);
            }
        },
        error: function (error){
            alert("Ocorreu um erro ao apagar essa sala!");
        }
    })
};



//Registrar novo espaço para café
function cadastrarEspacoCafe ()  {

    nome = $("#campoNomeCafe").val();

    var dados = JSON.stringify({nome: nome});

    // Enivo dos dados ao back-end para a inclusão
    $.ajax({
        url: 'http://localhost:5000/cadastrar_espaco_cafe',
        type: 'POST',
        dataType: 'json', contentType: 'application/json',
        data: dados, 
        success: espacoIncluido, 
        error: erroAoIncluir

    });
    function espacoIncluido (retorno) {
        if (retorno.resultado == "ok") { 
            alert(nome + " registrado com sucesso!");
            // Limpar o campo
            $("#campoNome").val("");
            popularCafeGeral();

        } 
        else {
            // informar mensagem de erro
            alert(retorno.resultado + ":" + retorno.detalhes);
        };            
    };
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        };
};

//Muda os dados no modal do espaço
function chamarModalCafeDelete(id_espaco_cafe){

    //$("#deleteCafeNome").val(espaco_nome);
    $("#modalCafeDeleteBtn").attr('onclick', ('apagarEspacoCafe('+id_espaco_cafe+ ')'));

}
//Apagar espaço para café baseado no ID
function apagarEspacoCafe(id_espaco_cafe){
    $.ajax({
        url: 'http://localhost:5000/apagar_espaco_cafe/'+id_espaco_cafe,
        type: 'DELETE',
        dataType: 'json', contentType: 'application/json',
        data: JSON.stringify({ id_espaco_cafe: id_espaco_cafe}), 
        success: function(retorno){
            if (retorno.resultado == "ok") {
                $("#trCafe_" + id_espaco_cafe).fadeOut(600, function(){ 
                alert("Espaço para café apagado com sucesso!"); 
                popularCafeGeral();
                
            });
            
        }
            else {
                alert(retorno.resultado + " : " + retorno.detalhes);
            }
        },
        error: function (error){
            alert("Ocorreu um erro ao apagar essa sala!");
        }
    })
};

//Muda os dados no modal da sala
function chamarModalSalaDelete(id_sala){

    //$("#deleteCafeNome").val(espaco_nome);
    $("#modalSalaDeleteBtn").attr('onclick', ('apagarSala('+id_sala+')'));

}
//Apagar sala baseado no ID
function apagarSala(id_sala){
    $.ajax({
        url: 'http://localhost:5000/apagar_sala/'+id_sala,
        type: 'DELETE',
        dataType: 'json', contentType: 'application/json',
        data: JSON.stringify({ id_sala: id_sala}), 
        success: function(retorno){
            if (retorno.resultado == "ok") {
                $("#trSala_" + id_sala).fadeOut(600, function(){ 
                alert("Sala apagada com sucesso!"); 
                popularSalasGeral();
                
            });
            
        }
            else {
                alert(retorno.resultado + " : " + retorno.detalhes);
            }
        },
        error: function (error){
            alert("Ocorreu um erro ao apagar essa sala!");
        }
    })
};


//Registrar nova pessoa
function cadastrarPessoa ()  {

    cpf = $("#campoCPF").val();
    cpf = String(cpf).replace(/[^\d]+/g,'');
    nome = $("#campoNome").val();
    sobrenome = $("#campoSobrenome").val();
    sala1_id = $("#selectSala1").val();
    cafe1_id = $("#selectCafe1").val();

    var dados = JSON.stringify({cpf: cpf, nome: nome, sobrenome: sobrenome, sala1_id : sala1_id, cafe1_id: cafe1_id, foto: null});

    // Enivo dos dados ao back-end para a inclusão
    $.ajax({
        url: 'http://localhost:5000/cadastrar_pessoa',
        type: 'POST',
        dataType: 'json', contentType: 'application/json',
        data: dados, 
        success: pessoaIncluida, 
        error: erroAoIncluir

    });
    function pessoaIncluida (retorno) {
        if (retorno.resultado == "ok") { 
            alert(nome + " registrado(a) com sucesso!");
            // Limpar os campo
            cpf = $("#campoCPF").val("");
            nome = $("#campoNome").val("");
            sobrenome = $("#campoSobrenome").val("");
            sala1_id = $("selectSala1").val("");
            cafe1_id = $("selectCafe1").val("");
            popularPessoasGeral();

        } 
        else {
            // informar mensagem de erro
            alert(retorno.resultado + ":" + retorno.detalhes);
        };            
    };
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        };
};

//Muda os dados no modal da pessoa
function chamarModalPessoaDelete(cpf){

    //$("#deleteCafeNome").val(espaco_nome);
    $("#modalPessoaDeleteBtn").attr('onclick', ('apagarPessoa('+cpf+')'));

}
//Apagar pessoa baseado no ID
function apagarPessoa(cpf){
    $.ajax({
        url: 'http://localhost:5000/apagar_pessoa/'+cpf,
        type: 'DELETE',
        dataType: 'json', contentType: 'application/json',
        data: JSON.stringify({ cpf: cpf}), 
        success: function(retorno){
            if (retorno.resultado == "ok") {
                $("#trPessoa_" + cpf).fadeOut(600, function(){ 
                alert("Pessoa apagada com sucesso!");
                popularPessoasGeral(); 
                
            });
            
        }
            else {
                alert(retorno.resultado + " : " + retorno.detalhes);
            }
        },
        error: function (error){
            alert("Ocorreu um erro ao apagar essa pessoa!");
        }
    })
};

