
function teste(){
    alert("Teste");
};

//Função para popular a tabela geral de pessoas
function popularPessoasGeral(){

    $.ajax({
        url: "http://localhost:5000/listar_pessoas",
        method: "GET",
        dataType: "json", 
        success: listar, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listar (pessoas) {

        
        // Define o texto para o total de salas
        $("#total_pessoas").text(pessoas.length)
        popularTabelaPessoas(pessoas,"#corpoTabelaPessoas")
      
    }

}

//Função para popular a tabela geral de salas
function popularSalasGeral(){

    $.ajax({
        url: "http://localhost:5000/listar_salas",
        method: "GET",
        dataType: "json", 
        success: listarsalas, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listarsalas (salas) {
        // Limpa os dados da tabela
        $("#corpoTabelaSalas").empty();    

        // Define o texto para o total de salas
        $("#total_salas").text(salas.length)
        
        // Percorre todas as salas registradas
        for (sala of salas){
            // Cria uma nova linha para cada sala
            lin = "<tr id='trSala_"+ sala.id_sala +"'>" + 
                "<td>" + (salas.indexOf(sala)+1) +"</td>" +
                "<td> <a href='sala_esp.html?id_sala=" + sala.id_sala + "'>"+ sala.nome + "</td>" + 
                "<td>" + sala.lotacao1+ "</td>" + 
                "<td>" + sala.lotacao2+ "</td>" + 
                "</a>"+
                "<td style='font-size: 1.5em'>" + 
                "<a href='#' title='Apagar' data-toggle='modal' data-target='#modalSalaDelete' onClick='chamarModalSalaDelete(" +sala.id_sala+");'>"+
                "<i class='fas fa-trash pr-1 text-danger'></i></a>" +
                "<a href='#' title='Editar' data-toggle='modal' data-target='#modalSalaEditar' onClick='chamarModalSalaEditar(" +sala.id_sala+");'>"+
                    "<i class='fas fa-edit text-primary'></i></a>" + 
                "</td>" +
            "</tr>"

            // Adiciona a nova linha na tabela
            $("#corpoTabelaSalas").append(lin);
        }
      
    }

}


//Função para popular a tabela geral de espaços para café
function popularCafeGeral(){

    $.ajax({
        url: "http://localhost:5000/listar_espacos_cafe",
        method: "GET",
        dataType: "json", 
        success: listar, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listar (espacos) {
        // Define o texto para o total de salas
        $("#total_espacos_cafe").text(espacos.length);
        popularTabelaCafe(espacos,"#corpoTabelaCafe");
      
    }

}

//Popula as opções de sala e espaço de café disponíveis para o cadastro
function popularSalasCadastro(){
    
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
        $("#selectCafe1").empty();    
        
        // Percorre todas os espaços registradas
        for (espaco of espacos){
            // Cria uma nova linha para cada espaço
           op =
           "<option value= '" + espaco.id_espaco+"'>"+ espaco.nome + "</option>"

            // Adiciona a nova linha na tabela
            $("#selectCafe1").append(op);
        }
      
    }

    //Pegar as opções de sala
    $.ajax({
        url: "http://localhost:5000/listar_sala1_disponiveis",
        method: "GET",
        dataType: "json", 
        success: listarsalas, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listarsalas (salas) {
        
        // Limpa os dados da tabela
        $("#selectSala1").empty();    
        
        // Percorre todas as salas registradas
        for (sala of salas){
            // Cria uma nova linha para cada sala
           op =
           "<option value= '" + sala.id_sala+"'>"+ sala.nome + "</option>"

            // Adiciona a nova linha na tabela
            $("#selectSala1").append(op);
        }
      
    }

}

//Função para popular os dados na página de uma sala específica
function dadosSala(){
    //Pega o ID através do link
    let id_sala = document.location.search.replace(/^.*?\=/,'');
    $.ajax({
        url: 'http://localhost:5000/dados_sala/'+id_sala,
        method: 'GET',
        dataType: 'json',
        success: function(resposta){
           $("#textNomeSala").text(resposta.nome)
           document.title += resposta.nome
        },
        error: function() {
            alert("Erro ao receber os dados da sala, verifique o backend!");
        }
    });
    //Pega as pessoas da primeira etapa
    $.ajax({
        url: "http://localhost:5000/pessoas_sala/"+id_sala+"/1",
        method: "GET",
        dataType: "json", 
        success: listar1, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listar1 (pessoas) {
        // Limpa os dados da tabela

        popularTabelaPessoas(pessoas,"#corpoTabelaPessoas1");
      
    }

    //Pega as pessoas da segunda etapa
    $.ajax({
        url: "http://localhost:5000/pessoas_sala/"+id_sala+"/2",
        method: "GET",
        dataType: "json", 
        success: listar2, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listar2 (pessoas) {
        // Limpa os dados da tabela

        popularTabelaPessoas(pessoas,"#corpoTabelaPessoas2");
      
    }
  
};


//Função para popular os dados na página de um espaço para café
function dadosCafe(){
    //Pega o ID através do link
    let id_espaco = document.location.search.replace(/^.*?\=/,'');
    $.ajax({
        url: 'http://localhost:5000/dados_cafe/'+id_espaco,
        method: 'GET',
        dataType: 'json',
        success: function(resposta){
           $("#textNomeCafe").text(resposta.nome)
           document.title += resposta.nome;

        },
        error: function() {
            alert("Erro ao receber os dados da sala, verifique o backend!");
        }
    });
    //Pega as pessoas da primeira etapa
    $.ajax({
        url: "http://localhost:5000/pessoas_cafe/"+id_espaco+"/1",
        method: "GET",
        dataType: "json", 
        success: listar1, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listar1 (pessoas) {
        // Limpa os dados da tabela  

        $("#total_espacos_cafe1").text(pessoas.length)

        // Percorre todas as pessoas registradas
        for (pessoa of pessoas){
            popularTabelaPessoas(pessoas,"#corpoTabelaPessoas1");
        }
      
    }

    //Pega as pessoas da segunda etapa
    $.ajax({
        url: "http://localhost:5000/pessoas_cafe/"+id_espaco+"/2",
        method: "GET",
        dataType: "json", 
        success: listar2, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listar2 (pessoas) {
        // Limpa os dados da tabela  

        $("#total_espacos_cafe2").text(pessoas.length);
        popularTabelaPessoas(pessoas,"#corpoTabelaPessoas2");
      
    }

};

function popularTabelaPessoas(pessoas,id_tabela){
    $(id_tabela).empty();  

    // Percorre todas as pessoas registradas
    for (pessoa of pessoas){

        // Cria uma nova linha para cada pessoa
        lin = "<tr id='trPessoa_"+pessoa.cpf+"'>" + 
        "<td>" + (pessoas.indexOf(pessoa)+1) +"</td>" +
        "<td>" + pessoa.cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4") + "</td>" + 
        "<td>" + pessoa.nome+ "</td>" + 
        "<td>" + pessoa.sobrenome+ "</td>" + 
        "<td> <a href='sala_esp.html?id_sala=" + pessoa.sala1.id_sala + "'>" + pessoa.sala1.nome+ "</td>" +
        "<td> <a href='sala_esp.html?id_sala=" + pessoa.sala2id_sala + "'>" + pessoa.sala2.nome+ "</td>" + 
        "<td> <a href='cafe_esp.html?id_sala=" + pessoa.cafe1.id_espaco + "'>" + pessoa.cafe1.nome+ "</td>" + 
        "<td> <a href='cafe_esp.html?id_sala=" + pessoa.cafe2.id_espaco + "'>" + pessoa.cafe2.nome+ "</td>" +  

        "<td style='font-size: 1.5em'>" + 
            "<a href='#' title='Apagar' data-toggle='modal' data-target='#modalPessoaDelete' onClick='chamarModalPessoaDelete(" +pessoa.cpf+");'>"+
            "<i class='fas fa-trash pr-1 text-danger'></i></a>" + 
            "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
        "</td>" +
        "</tr>"
        // Adiciona a nova linha na tabela
        $(id_tabela).append(lin);
    }

}

function popularTabelaCafe(espacos,id_tabela){
    // Limpa os dados da tabela
    $(id_tabela).empty();    
        
    // Percorre todas as espaço registradas
    for (espaco of espacos){
        // Cria uma nova linha para cada espaço
        lin = "<tr id='trCafe_"+ espaco.id_espaco +"'>" + 
            "<td>" + (espacos.indexOf(espaco)+1) +"</td>" +
            "<td> <a href='cafe_esp.html?id_espaco=" + espaco.id_espaco + "'>"+ espaco.nome + "</td>" + 
            "<td>" + espaco.lotacao1+ "</td>" + 
            "<td>" + espaco.lotacao2+ "</td>" + 

            "<td style='font-size: 1.5em'>" + 
            "<a href='#' title='Apagar' data-toggle='modal' data-target='#modalCafeDelete' onClick='chamarModalCafeDelete(" +espaco.id_espaco+");'>"+
                "<i class='fas fa-trash pr-1 text-danger'></i></a>" + 
            "<a href='#' title='Editar' data-toggle='modal' data-target='#modalCafeEditar' onClick='chamarModalCafeEditar(" +espaco.id_espaco+");'>"+
                "<i class='fas fa-edit text-primary'></i></a>" + 
            "</td>" +
        "</tr>"

        // Adiciona a nova linha na tabela
        $(id_tabela).append(lin);
    }
}