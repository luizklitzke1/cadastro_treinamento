
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
            alert("Erro ao buscar os dados no backend ");
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
                "<a href='#' title='Apagar'><i class='fas fa-trash pr-1 text-danger'></i></a>" + 
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
            alert("Erro ao buscar os dados no backend ");
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
            lin = "<tr>" + 
                "<td>" + (salas.indexOf(sala)+1) +"</td>" +
                "<td>" + sala.nome + "</td>" + 
                "<td>" + sala.lotacao1+ "</td>" + 
                "<td>" + sala.lotacao2+ "</td>" + 

                "<td style='font-size: 1.5em'>" + 
                    "<a href='#' title='Apagar'><i class='fas fa-trash pr-1 text-danger'></i></a>" + 
                    "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
                "</td>" +
            "</tr>"

            // Adiciona a nova linha na tabela
            $("#corpoTabelaSalas").append(lin);
        }
      
    }

}

