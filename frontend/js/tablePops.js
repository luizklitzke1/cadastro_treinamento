
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
        // Limpa os dados da tablea
        $("#corpoTabelaPessoas").empty();    

        // Define o texto para o total de salas
        $("#total_pessoas").text(pessoas.length)
        
        // Percorre todas as pessoas registradas
        for (pessoa of pessoas){
            // Cria uma nova linha para cada pessoa
            lin = "<tr>" + 
            "<td>" + (pessoas.indexOf(pessoa)+1) +"</td>" +
            "<td>" + pessoa.cpf + "</td>" + 
            "<td>" + pessoa.nome+ "</td>" + 
            "<td>" + pessoa.sobrenome+ "</td>" + 
            "<td>" + pessoa.sala1.nome+ "</td>" +
            "<td>" + pessoa.sala2.nome+ "</td>" + 
            "<td>" + pessoa.cafe1.nome+ "</td>" + 
            "<td>" + pessoa.cafe2.nome+ "</td>" +  

            "<td style='font-size: 1.5em'>" + 
                "<a href='#' title='Apagar' data-toggle='modal' data-target='#modalPessoaDelete' onClick='chamarModalPessoaDelete(" +pessoa.cpf+");'>"+
                "<i class='fas fa-trash pr-1 text-danger'></i></a>" + 
                "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
            "</td>" +
            "</tr>"

            // Adiciona a nova linha na tabela
            $("#corpoTabelaPessoas").append(lin);
        }
      
    }

}

//Função para popular a tabela geral de salas
function popularSalasGeral(){

    $.ajax({
        url: "http://localhost:5000/listar_salas",
        method: "GET",
        dataType: "json", 
        success: listar, 
        error: function(problema) {
            alert("Erro ao buscar os dados no backend! ");
        }
    });
    function listar (salas) {
        // Limpa os dados da tablea
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
                    "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
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
        // Limpa os dados da tablea
        $("#corpoTabelaCafe").empty();    

        // Define o texto para o total de salas
        $("#total_espacos_cafe").text(espacos.length)
        
        // Percorre todas as espaço registradas
        for (espaco of espacos){
            // Cria uma nova linha para cada espaço
            lin = "<tr id='trCafe_"+ espaco.id_espaco +"'>" + 
                "<td>" + (espacos.indexOf(espaco)+1) +"</td>" +
                "<td>" + espaco.nome + "</td>" + 
                "<td>" + espaco.lotacao1+ "</td>" + 
                "<td>" + espaco.lotacao2+ "</td>" + 

                "<td style='font-size: 1.5em'>" + 
                "<a href='#' title='Apagar' data-toggle='modal' data-target='#modalCafeDelete' onClick='chamarModalCafeDelete(" +espaco.id_espaco+");'>"+
                    "<i class='fas fa-trash pr-1 text-danger'></i></a>" + 
                    "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
                "</td>" +
            "</tr>"

            // Adiciona a nova linha na tabela
            $("#corpoTabelaCafe").append(lin);
        }
      
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
        // Limpa os dados da tablea
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
        
        // Limpa os dados da tablea
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
        },
        error: function() {
            alert("Erro ao receber os dados da sala, verifique o backend!");
        }
    });
    //Pega os alunos da primeira etapa
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
        // Limpa os dados da tablea
        $("#corpoTabelaPessoas1").empty();    

        // Percorre todas as pessoas registradas
        for (pessoa of pessoas){
            // Cria uma nova linha para cada pessoa
            lin = "<tr>" + 
            "<td>" + (pessoas.indexOf(pessoa)+1) +"</td>" +
            "<td>" + pessoa.cpf + "</td>" + 
            "<td>" + pessoa.nome+ "</td>" + 
            "<td>" + pessoa.sobrenome+ "</td>" + 

            "<td style='font-size: 1.5em'>" + 
                "<a href='#' title='Apagar' data-toggle='modal' data-target='#modalPessoaDelete' onClick='chamarModalPessoaDelete(" +pessoa.cpf+");'>"+
                "<i class='fas fa-trash pr-1 text-danger'></i></a>" + 
                "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
            "</td>" +
            "</tr>"

            // Adiciona a nova linha na tabela
            $("#corpoTabelaPessoas1").append(lin);
        }
      
    }

    //Pega os alunos da segunda etapa
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
        // Limpa os dados da tablea
        $("#corpoTabelaPessoas2").empty();    

        // Percorre todas as pessoas registradas
        for (pessoa of pessoas){
            // Cria uma nova linha para cada pessoa
            lin = "<tr>" + 
            "<td>" + (pessoas.indexOf(pessoa)+1) +"</td>" +
            "<td>" + pessoa.cpf + "</td>" + 
            "<td>" + pessoa.nome+ "</td>" + 
            "<td>" + pessoa.sobrenome+ "</td>" + 

            "<td style='font-size: 1.5em'>" + 
                "<a href='#' title='Apagar' data-toggle='modal' data-target='#modalPessoaDelete' onClick='chamarModalPessoaDelete(" +pessoa.cpf+");'>"+
                "<i class='fas fa-trash pr-1 text-danger'></i></a>" + 
                "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
            "</td>" +
            "</tr>"

            // Adiciona a nova linha na tabela
            $("#corpoTabelaPessoas2").append(lin);
        }
      
    }

  
};

