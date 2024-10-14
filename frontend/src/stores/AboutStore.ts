import { defineStore } from 'pinia'
export const AboutStore:any  = defineStore('about', {
    state: () => ({
       abouts: []
    }),
    getters: {
        allAbouts(state) {
            this.getallAbouts()
            return state.abouts
        },
        getSocialsById: (state) => {
            return (user_id: number) => state.abouts[0].find((el: dict) => el.id === user_id).socials;
        },
        getPicById: (state) => {
            return (user_id: number ) => state.abouts[0].find((el: dict) => el.id === user_id).photo_link;
        }
    },
    actions: {
            getallAbouts(): Promise<number> {
                return fetch('http://127.0.0.1:5000/about')
                    .then((response) => response.json())
                    .then((data: JSON) => this.abouts.push(data["message"]))
            },
        },
})