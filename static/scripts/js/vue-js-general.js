var app = new Vue({
    el: '#app',
    data: {
        menuStatus: 'closed'
    },
    methods: {
        openMenu: function () {
            this.menuStatus = 'opened'
        },
        closeMenu: function () {
            this.menuStatus = 'closed'
        }
    }
});
