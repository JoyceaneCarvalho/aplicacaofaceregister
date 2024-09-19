    document.getElementById('cadastroForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Impede o envio do formulário

      // Captura os dados do formulário
      const nome = document.getElementById('nome').value;
      const matricula = document.getElementById('matricula').value;
      const curso = document.getElementById('curso').value;
      const email = document.getElementById('email').value;
      const foto = document.getElementById('foto').files[0];
      const userType = document.querySelector('input[name="userType"]:checked').value;

      // Armazenar os dados no localStorage para carregá-los na próxima página
      localStorage.setItem('nome', nome);
      localStorage.setItem('matricula', matricula);
      localStorage.setItem('curso', curso);
      localStorage.setItem('email', email);

      // Se a foto for selecionada, gerar uma URL temporária e salvar no localStorage
      if (foto) {
        const fotoURL = URL.createObjectURL(foto);
        localStorage.setItem('foto', fotoURL);
      }

      // Redirecionar de acordo com o tipo de usuário
      if (userType === 'aluno') {
        window.location.href = 'cadastro/perfilaluno.html'; // Redireciona para a página do aluno
      } else if (userType === 'professor') {
        window.location.href = 'perfilprofessor.html'; // Redireciona para a página do professor
      } else {
        alert('Tipo de usuário não reconhecido.');
      }
    });
