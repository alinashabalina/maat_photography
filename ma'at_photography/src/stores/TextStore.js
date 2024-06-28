import { defineStore } from 'pinia'
export const useTextStore = defineStore('text', {
    state: () => ({
        mainText: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eu velit risus. Vestibulum cursus mauris sed rutrum dictum. Donec quis tellus at mi pulvinar vestibulum. Phasellus ultricies nibh ac libero molestie, sit amet elementum odio commodo. Curabitur eleifend egestas dui vel aliquet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam vitae arcu a quam hendrerit semper. Sed a tincidunt mauris. Donec efficitur semper fermentum. Suspendisse ornare, massa eu placerat dapibus, neque nibh hendrerit urna, vel finibus quam dui nec elit. Etiam ante quam, fermentum quis blandit ac, vehicula in nulla. Curabitur non urna ante. Duis viverra volutpat elit.\n" +
            "\n" +
            "    Duis ut malesuada metus, non mattis elit. Suspendisse molestie enim urna, quis finibus tortor porta in. Aliquam eu imperdiet mi. Praesent eleifend ex accumsan sagittis ornare. Mauris id mattis erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam vel nunc varius, sodales ipsum eu, venenatis leo. In ipsum ex, cursus dignissim iaculis sed, feugiat ut augue. Donec aliquet ex sed tristique tristique. In tempus rhoncus lacus sed sollicitudin. Integer congue diam sem, a lobortis quam molestie vel. Quisque sit amet rhoncus felis. Etiam efficitur, est non imperdiet placerat, turpis ex lobortis nibh, vel venenatis tortor tellus in quam.\n" +
            "\n" +
            "    Morbi ex ipsum, rhoncus quis diam in, dapibus rhoncus nibh. Vestibulum non nibh justo. Maecenas faucibus nulla non rutrum luctus. Integer lobortis dui eget finibus imperdiet. Vivamus a nisl ac justo porta interdum a in neque. Sed malesuada scelerisque nulla, in euismod libero finibus semper. Aliquam mattis enim vel est dictum, ut suscipit ex finibus. Praesent aliquam finibus dictum."
    }),
    getters: {
        getTextMain(state) {
            return state.mainText
        },
    },
    actions: {
        getArticleText() {
        },
    },
})
