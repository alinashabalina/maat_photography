import { defineStore } from 'pinia'
export const AboutStore = defineStore('gallery', {
    state: () => ({
    }),
    getters: {

    },
    actions: {
        getallAbouts() {
            return fetch('http://127.0.0.1:5000/about')
                .then((response) => response.json())
                .then((data) => this.abouts.push(data["message"]))
        },
    },
})