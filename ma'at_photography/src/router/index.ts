import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RestoreView from '../views/RestoreView.vue'
import AboutView from '../views/AboutView.vue'
import JoinView from "../views/JoinView.vue";
import GalleryView from "../views/GalleryView.vue";
import IssueView from "../views/IssueView.vue";
import IssueMainArticleView from "../views/IssueMainArticleView.vue";
import IssueGalleryView from "../views/IssueGalleryView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/restore',
            name: 'restore',
            component: RestoreView
        },
        {
            path: '/about',
            name: 'about',
            component: AboutView
        },
        {
            path: '/join',
            name: 'join',
            component: JoinView
        },
        {
            path: '/gallery',
            name: 'gallery',
            component: GalleryView
        },
        {
            path: '/issue/:id',
            component: IssueView,
        },
        {
            path: '/issue/:id/article',
            name: "article",
            component: IssueMainArticleView,
        },
        {
            path: '/issue/:id/gallery',
            component: IssueGalleryView,
        }
    ]
})

export default router
