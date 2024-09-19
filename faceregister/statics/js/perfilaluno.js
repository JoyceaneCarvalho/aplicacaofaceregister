   document.addEventListener("DOMContentLoaded", function() {
      const nome = localStorage.getItem('nome');
      const matricula = localStorage.getItem('matricula');
      const curso = localStorage.getItem('curso');
      const email = localStorage.getItem('email');
      const foto = localStorage.getItem('foto');

      if (nome && matricula && curso && email && foto) {
        document.getElementById('profileNome').textContent = nome;
        document.getElementById('profileMatricula').textContent = matricula;
        document.getElementById('profileCurso').textContent = curso;
        document.getElementById('profileEmail').textContent = email;
        document.getElementById('profileFoto').src = foto;
      } else {
        alert('Nenhum dado encontrado. Por favor, preencha o cadastro.');
        window.location.href = 'cadastroaluno.html'; // Redireciona de volta ao cadastro se não houver dados
      }
    });