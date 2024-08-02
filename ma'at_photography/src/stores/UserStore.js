import { defineStore } from 'pinia'
export const AboutStore = defineStore('user', {
    state: () => ({
        user: []
    }),
    getters: {

    },
    actions: {
        getUserData(user_id) {
            return fetch(` http://127.0.0.1:5000/user/${user_id}` )
                .then((response) => response.json())
                .then((data) => {this.user.push(data["user_info"])})
        },
    },
})