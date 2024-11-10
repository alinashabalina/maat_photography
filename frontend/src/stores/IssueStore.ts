import { defineStore } from 'pinia'
import { mande } from 'mande'

const abouts = mande("http://127.0.0.1:5000/issues")
export const AboutStore:any  = defineStore('issues', {
    state: () => ({
        issues: [] as Issues[],
    }),
    actions: {
        async getallIssues() {
            try {
                await abouts.get()
                    .then((data: any) => {this.abouts.push(data["message"]);return this.abouts})}
            catch (error) {
                return error
            }
        },
    },
})

interface Issues {
    id: number,
    name: String,
    social: String,
    photo_link: String,
}