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
            $("#campoNomeSala").val(""); 
            alert("Sala " + nome + " registrada com sucesso!");
            // Limpar o campo
            popularSalasGeral();popularPessoasGeral();popularCafeGeral();

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
                popularSalasGeral();popularPessoasGeral();popularCafeGeral();
                
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

//Editar sala baseado no ID
function editarSala(id_sala){

    novo_nome = $("#campoNomeSalaEditar").val();
    var dados = JSON.stringify({novo_nome: novo_nome});

    // Enivo dos dados ao back-end para a inclusão
    $.ajax({
        url: 'http://localhost:5000/editar_sala/'+id_sala,
        type: 'POST',
        dataType: 'json', contentType: 'application/json',
        data: dados, 
        success: salaEditada, 
        error: erroAoIncluir

    });
    function salaEditada (retorno) {
        if (retorno.resultado == "ok") { 
            alert("Sala editada  com sucesso!");
            // Limpar o campo
            $("#campoNomeSalaEditar").val("");
            if ($('#textNomeSala').length > 0) {
                location.reload();
            }
            else{
                popularSalasGeral();popularPessoasGeral();popularCafeGeral();
            }
            
            
            
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

//Editar espaço para café baseado no ID
function editarCafe(id_cafe){

    novo_nome = $("#campoNomeCafeEditar").val();
    var dados = JSON.stringify({novo_nome: novo_nome});

    // Enivo dos dados ao back-end para a inclusão
    $.ajax({
        url: 'http://localhost:5000/editar_cafe/'+id_cafe,
        type: 'POST',
        dataType: 'json', contentType: 'application/json',
        data: dados, 
        success: cafeEditado, 
        error: erroAoIncluir

    });
    function cafeEditado (retorno) {
        if (retorno.resultado == "ok") { 
            alert("Espaço para café editado  com sucesso!");
            // Limpar o campo
            $("#campoNomeCafeEditar").val("");
            if ($('#textNomeCafe').length > 0) {
                location.reload();
            }
            else{
                popularSalasGeral();popularPessoasGeral();popularCafeGeral();
            }
            
            
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
            $("#campoNomeCafe").val("");
            popularSalasGeral();popularPessoasGeral();popularCafeGeral();

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


//Muda os dados no modal do espaço
function chamarModalPessoaEditar(cpf){

    //$("#deleteCafeNome").val(espaco_nome);
    $("#btnEditarPessoa").attr('onclick', ('editarPessoa('+cpf+ ')'));

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

    $("#modalSalaDeleteBtn").attr('onclick', ('apagarSala('+id_sala+')'));

}

//Muda os dados no modal da sala
function chamarModalSalaEditar(id_sala){

    $("#btnEditarSala").attr('onclick', ('if (checkFormSala2()) {editarSala('+id_sala+');popularSalasGeral();};'));

}

//Muda os dados no modal de um espaço para café
function chamarModalCafeEditar(id_espaco){

    $("#btnEditarCafe").attr('onclick', ('if (checkFormCafe2()) {editarCafe('+id_espaco+');popularCafeGeral();};'));

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
                popularSalasGeral();popularPessoasGeral();popularCafeGeral();
                
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
            popularSalasGeral();popularPessoasGeral();popularCafeGeral();

        } 
        else {
            // informar mensagem de erro
            alert("Ocorreu um erro ao cadastrar a pessoa! Verifique se o CPF já não é cadastrado!");
        };            
    };
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("Ocorreu um erro ao cadastrar a pessoa! Verifique se o CPF já não é cadastrado!");
        };
};

//Muda os dados no modal da pessoa
function chamarModalPessoaDelete(cpf){

    //$("#deleteCafeNome").val(espaco_nome);
    $("#modalPessoaDeleteBtn").attr('onclick', ("apagarPessoa('"+cpf+"')"));

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
                popularSalasGeral();popularPessoasGeral();popularCafeGeral();
                
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


//Editar pessoa  baseado no CPF
function editarPessoa(cpf){

    
    novo_cpf = $("#campoCPFPessoaEditar").val();
    novo_cpf = String(cpf).replace(/[^\d]+/g,'')
    novo_nome = $("#campoNomePessoaEditar").val();
    novo_sobrenome = $("#campoSobrenomePessoaEditar").val();
    var dados = JSON.stringify({novo_cpf: novo_cpf, novo_nome: novo_nome, novo_sobrenome: novo_sobrenome});

    // Enivo dos dados ao back-end para a inclusão
    $.ajax({
        url: 'http://localhost:5000/editar_pessoa/'+cpf,
        type: 'POST',
        dataType: 'json', contentType: 'application/json',
        data: dados, 
        success: pessoaEditada, 
        error: erroAoIncluir

    });
    function pessoaEditada (retorno) {
        if (retorno.resultado == "ok") { 
            alert("Pessoa editada com sucesso!");
            // Limpar o campo
            $("#campoCPFPessoaEditar").val("");
            $("#campoNomePessoaEditar").val("");
            $("#campoSobrenomePessoaEditar").val("");
            popularSalasGeral();popularPessoasGeral();popularCafeGeral();
            
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
