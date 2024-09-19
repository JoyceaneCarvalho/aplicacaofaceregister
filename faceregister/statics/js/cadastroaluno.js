      function handleSubmit(event) {
      event.preventDefault();

      const nome = document.getElementById('nome').value;
      const matricula = document.getElementById('matricula').value;
      const curso = document.getElementById('curso').value;
      const email = document.getElementById('email').value;
      const foto = document.getElementById('foto').files[0];

      const reader = new FileReader();
      reader.onload = function(e) {
        // Salvando dados no localStorage
        localStorage.setItem('nome', nome);
        localStorage.setItem('matricula', matricula);
        localStorage.setItem('curso', curso);
        localStorage.setItem('email', email);
        localStorage.setItem('foto', e.target.result);

        // Redirecionando para a página de perfil
        window.location.href = "{% url 'perfilaluno' %}";
      };
      reader.readAsDataURL(foto);
    }