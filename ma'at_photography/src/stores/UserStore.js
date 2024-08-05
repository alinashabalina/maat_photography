import { defineStore } from 'pinia'
export const UserStore = defineStore('user', {
    state: () => ({
        user: []
    }),
    getters: {
        getData() {
            return (user_id) =>
            this.getUserData(user_id)

        },
        getDetails(state) {
            return state.user
        }

    },
    actions: {
        getUserData(user_id) {
            fetch(` http://127.0.0.1:5000/user/${user_id}` )
                .then((response) => response.json())
                .then((data) => this.user.push(data["user_info"]))
        },
    },
})