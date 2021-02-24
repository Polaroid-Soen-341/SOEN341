<template>
    <div>
        <v-navigation-drawer color="deep-purple darken-2" app v-model="drawer">
          <v-sheet color="grey lighten-4"
                   class="pa-4">
            <v-avatar class="mb-4"
                      color="grey darken-1"
                      size="64">
            </v-avatar>

            <div>Username</div>
          </v-sheet>

          <v-divider></v-divider>

          <v-list nav
                  dense
                  class="white--text">
            <v-list-item-group v-model="selectedItem"
                               color="white">
              <v-list-item v-for="(item, i) in items"
                           :key="i"
                           class="white--text"
                           @click="redirect()">
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>

                <v-list-item-content class="white--text">
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>

        <v-app-bar class="white--text" color="deep-purple darken-4" app>
          <v-app-bar-nav-icon color="white" @click="drawer = !drawer"></v-app-bar-nav-icon>
          <div class="text-h6 pl-2" style="font-family: 'Playfair Display', serif;">
            Polaroid
          </div>
          <v-icon
            class="ml-2"
            large
            color="white">
            mdi-instagram
          </v-icon>
          <v-btn
            class="ma-2"
            outlined
            style="position: absolute; right: 4px"
            color="white"
            @click="logout()">
              Logout
          </v-btn>
        </v-app-bar>

        <!-- Sizes your content based upon application components -->
        <v-main>

          <!-- Provides the application the proper gutter -->
          <v-container fluid>

            <!-- If using vue-router -->
            <router-view></router-view>
          </v-container>
        </v-main>

        <v-footer color="deep-purple darken-4" app>
          <!-- -->
        </v-footer>
    </div>
</template>

<script>
export default {
  name: "MainLayout",
  // mounted() {
  //   this.checkLoggedIn();
  // },
  data: () => ({
    drawer: null,
    selectedItem: null,
    items: [
      { id: 0, text: 'My Feed', path: 'feed', icon: 'mdi-view-list' },
      { id: 1, text: 'My Posts', path: 'feed', icon: 'mdi-send' },
      { id: 2, text: 'Notifications', path: 'feed', icon: 'mdi-bell' },
      { id: 3, text: 'Settings', path: 'feed', icon: 'mdi-cog' }
    ]
  }),
  methods: {
    // redirect(){
    //   console.log(this.items[this.selectedItem])
    //   this.$router.push(this.items[this.selectedItem].path)
    // },
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        this.$router.push('/');
      }
    },
    logout: function () {
      this.$session.destroy()
      this.$router.push('/')
    }
  }
};
</script>
