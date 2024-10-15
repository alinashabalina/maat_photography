import { defineStore } from 'pinia'
import { mande } from 'mande'

const abouts = mande("http://127.0.0.1:5000/about")
export const AboutStore:any  = defineStore('about', {
    state: () => ({
       abouts: [] as Abouts[],
    }),
    actions: {
        async getallAbouts() {
            try {
                await abouts.get()
                    .then((data: any) => {this.abouts.push(data["message"]);return this.abouts})}
            catch (error) {
                return error
            }
        },
    },
})

interface Abouts {
    id: number,
    name: String,
    social: String,
    photo_link: String,
}