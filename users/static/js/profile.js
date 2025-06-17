<script>
  document.querySelectorAll(".delete-profile-btn").forEach(button => {
    button.addEventListener("click", function () {
      const profileId = this.getAttribute("data-profile-id");
      const confirmModal = document.getElementById("confirm-modal");
      confirmModal.classList.add("active");

      document.getElementById("confirm-delete-btn").onclick = function () {
        // Cria e envia um form via POST
        const form = document.createElement("form");
        form.method = "POST";
        form.action = "/profile/";

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        form.innerHTML = `
          <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
          <input type="hidden" name="action" value="delete">
          <input type="hidden" name="profile_id" value="${profileId}">
        `;
        document.body.appendChild(form);
        form.submit();
      };

      document.getElementById("cancel-delete-btn").onclick = function () {
        confirmModal.classList.remove("active");
      };
    });
  });

  // Editar (abrir modal com dados)
  document.querySelectorAll(".edit-profile-btn").forEach(button => {
    button.addEventListener("click", function () {
      const profileId = this.getAttribute("data-profile-id");
      // Aqui você deve preencher o modal com os dados do perfil via AJAX ou template JS
      document.getElementById("modal").classList.add("active");
      document.getElementById("modal-title").innerText = "Editar Perfil";
      document.getElementById("form-submit-btn").innerText = "Salvar Alterações";
      document.getElementById("profile-action").value = "edit";
      document.getElementById("profile-id").value = profileId;

      // Dica: use dataset para preencher nome/email/avatar se estiver disponível no HTML
    });
  });
</script>
