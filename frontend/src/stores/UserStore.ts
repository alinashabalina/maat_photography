import { defineStore } from 'pinia'
import { mande } from 'mande'

let user_id: number | null = null;
const user = mande(`http://127.0.0.1:5000/user/${user_id}`)
export const UserStore:any  = defineStore('user', {
    state: () => ({
        user: [] as User[],
    }),
    getters: {
    },

    actions: {
        async getUser(user_id:number): Promise<any> {
            try {
                await user.get(user_id)
                    .then((data: any) => {this.user.push(data["user_info"]);return this.user})}
            catch (error) {
                return error
            }
        },
    },
})

interface User {
    user_favorites: [],
    user_id: number,
    user_orders: [],
    user_reads: []
}