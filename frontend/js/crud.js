//Registrar nova sala
function cadastrarSala ()  {

    nome = $("#campoNome").val();

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

    nome = $("#campoNome").val();

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


function chamarModalCafeDelete(id_espaco_cafe){

    //$("#deleteCafeNome").val(espaco_nome);
    $("#modalCafeDeleteBtn").attr('onclick', ('apagarEspacoCafe('+id_espaco_cafe+ ')'));

}
//Apagar sala baseado no ID
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

