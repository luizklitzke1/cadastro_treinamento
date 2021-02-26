//Script responsável pela pesquisa em tempo real dos dados baseado em inputs no front


//Muda a mensagem de erro nos inputs
function msg(id,message){
    $(id).text(message).show;
}

//Mostra a div com a msg
function show(id){
    $(id).show();
}


//Verificação customizada do nome
var testeLetters = new RegExp(/^[\s\d\p{L}]*$/ui);

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
            success: listarSalasProcura, 
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


$("#procurarCafe").on('input', function() {

    var input= $(this);
    nome = input.val();

    if (testeLetters.test(nome)){
       //Função para popular a tabela geral de espaços para café
       
       var dados = JSON.stringify({nome : nome});

        $.ajax({
            url: "http://localhost:5000/procurar_cafe",
            method: "POST",
            dataType: 'json', contentType: 'application/json',
            data: dados,  
            success: listarCafeProcura, 
            error: function(problema) {
                alert("Erro ao buscar os dados no backend! ");
            }
        });
        function listarCafeProcura (espacos) {
            // Limpa os dados da tabela
            $("#corpoTabelaCafe").empty();    
            
            // Percorre todas as salas registradas
            try{
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
                        "<a href='#' title='Editar'><i class='fas fa-edit text-primary'></i></a>" + 
                    "</td>" +
                    "</tr>"

                    // Adiciona a nova linha na tabela
                    $("#corpoTabelaCafe").append(lin);
                }
            
            }
            catch{
               
            }
          
        }
    }
    
    else{
        msg("#inv-nome-sala-procura","O nome deve conter apenas letras!");
        
    };

    
});


//Não encontrei maneira melhor de setar o attr pra todos de uma vez só
//E apenas chamando a função, sem declarar outra, ela não da trigger...
$("#procurarPessoaCPF").on('input', function() {procurar_pessoa()})
$("#procurarPessoaNome").on('input', function() {procurar_pessoa()})
$("#procurarPessoaSobrenome").on('input', function() {procurar_pessoa()})

function procurar_pessoa(){

    cpf = $("#procurarPessoaCPF").val();
    nome = $("#procurarPessoaNome").val();
    sobrenome= $("#procurarPessoaSobrenome").val();

    if (testeLetters.test(cpf) && testeLetters.test(nome) && testeLetters.test(sobrenome)){
       //Função para popular a tabela geral de espaços para café
        var dados = JSON.stringify({cpf: cpf, nome : nome, sobrenome : sobrenome});
        $.ajax({
            url: "http://localhost:5000/procurar_pessoa",
            method: "POST",
            dataType: 'json', contentType: 'application/json',
            data: dados,  
            success: listarPessoasProcura, 
            error: function(problema) {
                alert("Erro ao receber os dados do backend!");
            }
        });
        function listarPessoasProcura (pessoas) {
            // Limpa os dados da tabela
            $("#corpoTabelaPessoas").empty();    
            
            // Percorre todas as salas registradas
            try{
                // Percorre todas as pessoas registradas
                for (pessoa of pessoas){
                    // Cria uma nova linha para cada pessoa
                    lin = "<tr id='trPessoa_"+pessoa.cpf+"'>" + 
                    "<td>" + (pessoas.indexOf(pessoa)+1) +"</td>" +
                    "<td>" + pessoa.cpf + "</td>" + 
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
                    $("#corpoTabelaPessoas").append(lin);
                }
            
            }
            catch{
               
            }
          
        }
    }
    
    else{
        msg("#inv-nome-sala-procura","O nome deve conter apenas letras!");
        
    };

    
};




