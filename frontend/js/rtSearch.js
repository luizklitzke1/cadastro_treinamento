//Script para declaração e controle da validação dos forumários de salas e espaços de facé em tempo real
// Separado do padrão de HTML para melhor customização e controle


//Muda a mensagem de erro nos inputs
function msg(id,message){
    $(id).text(message).show;
}

//Mostra a div com a msg
function show(id){
    $(id).show();
}


//Verificação customizada do nome
var testeLetters = new RegExp(/^[\s\p{L}]*$/ui);

$("#procurarSala").on('input', function() {

    var input= $(this);
    nome = input.val();

    if (testeLetters.test(nome)){
       //Função para popular a tabela geral de espaços para café
       
       var dados = JSON.stringify({nome : nome});

        $.ajax({
            url: "http://localhost:5000/procurar_sala",
            method: "POST",
            dataType: 'json', contentType: 'application/json',
            data: dados,  
            success: listarSalasProcura(), 
            error: function(problema) {
                alert("Erro ao buscar os dados no backend! ");
            }
        });
        function listarSalasProcura (salas) {
            // Limpa os dados da tabela
            $("#corpoTabelaSalas").empty();    
            
            // Percorre todas as salas registradas
            try{
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
                $("#corpoTabelaSalas").append(lin);}
            
            }
            catch{
               
            }
          
        }
    }
    
    else{
        msg("#inv-nome-sala-procura","O nome deve conter apenas letras!");
        
    };

    
});




