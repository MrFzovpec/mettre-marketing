var app = new Vue({
    el: '#app',
    data: {
        username: null,
        password: '',
        email: '',
        confirm_password: '',
        current_screen: 0,
        selected_social: null,
        social_url: null,
        check_user: {
            username: true,
            password: true,
            email: true
        }
    },
    methods: {
        usernameCheck: function () {
            axios
                .get(`/check-username?username=${this.username}`)
                .then(response => this.check_user.username = response.data.user_status)
        },
        emailCheck: function () {
            axios
                .get(`/check-email?email=${this.email}`)
                .then(response => this.check_user.email = response.data.user_status)
        },
        nextScreen: function () {
            this.current_screen += 1
        },
        customSubmit: function () {
            this.current_screen += 1;
            document.querySelector('form.loginForm').style.display = 'none';
        },
        prevScreen: function () {
            this.current_screen -= 1
        },

    }
});
