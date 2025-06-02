document.addEventListener('DOMContentLoaded', () => {
  // Gerenciador principal de perfis
  class ProfileManager {
    constructor() {
      this.initProfileModal();
      this.initAvatarModal();
      this.initProfileButtons();
    }

    // Modal de criação de perfil
    initProfileModal() {
      const openProfileModalBtn = document.getElementById('open-modal-btn');
      const profileModal = document.getElementById('modal');
      const closeProfileModalBtn = document.getElementById('close-modal-btn');

      openProfileModalBtn?.addEventListener('click', () => {
        profileModal.classList.add('active');
        document.body.style.overflow = 'hidden';
      });

      closeProfileModalBtn?.addEventListener('click', () => {
        profileModal.classList.remove('active');
        document.body.style.overflow = 'auto';
      });

      window.addEventListener('click', (e) => {
        if (e.target === profileModal) {
          profileModal.classList.remove('active');
          document.body.style.overflow = 'auto';
        }
      });
    }

    // Modal de seleção de avatar
    initAvatarModal() {
      const avatarModal = document.getElementById('avatar-modal');
      const openAvatarModalBtn = document.getElementById('change-avatar-btn');
      const closeAvatarModalBtn = document.getElementById('close-avatar-modal');
      const selectedAvatar = document.getElementById('selected-avatar');
      const avatarInput = document.getElementById('avatar');

      openAvatarModalBtn?.addEventListener('click', () => {
        avatarModal.classList.add('active');
        document.body.style.overflow = 'hidden';
      });

      closeAvatarModalBtn?.addEventListener('click', () => {
        avatarModal.classList.remove('active');
        document.body.style.overflow = 'auto';
      });

      const avatarCircles = avatarModal.querySelectorAll('.avatar-circle');

      avatarCircles.forEach(circle => {
        circle.addEventListener('click', () => {
          // Remove seleção anterior
          avatarCircles.forEach(c => c.classList.remove('selected'));
          
          // Marca seleção atual
          circle.classList.add('selected');

          // Atualiza o avatar
          const avatarName = circle.dataset.avatar;
          selectedAvatar.style.backgroundImage = `url('{% static "avatars/" %}${avatarName}')`;
          
          // Atualiza o campo hidden
          if (avatarInput) {
            avatarInput.value = avatarName;
          }

          // Animação de confirmação
          circle.classList.add('animate__animated', 'animate__bounceIn');
          setTimeout(() => {
            circle.classList.remove('animate__animated', 'animate__bounceIn');
          }, 1000);

          // Fecha o modal após um pequeno delay
          setTimeout(() => {
            avatarModal.classList.remove('active');
            document.body.style.overflow = 'auto';
          }, 500);
        });
      });
    }

    // Efeitos nos botões de perfil existentes
    initProfileButtons() {
      const profileButtons = document.querySelectorAll('.profile-button');
      
      profileButtons.forEach(button => {
        button.addEventListener('mouseenter', () => {
          button.classList.add('animate__animated', 'animate__pulse');
        });
        
        button.addEventListener('mouseleave', () => {
          button.classList.remove('animate__animated', 'animate__pulse');
        });
      });
    }
  }

  // Inicializa o gerenciador de perfis
  new ProfileManager();
});