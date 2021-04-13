<template>
    <v-container grid-list-sm>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm12 lg12 md12>
          <v-card class="mx-12 mt-2">
            <v-card-title class="black--text pl-4">
              <v-avatar
                color="blue"
                size="100">
                <span class="white--text">{{ user }}</span>
              </v-avatar>
              <div>
                <div class="pb-2">
                  <span class="text-h5 headline px-4" align="left">{{ userInfo.first_name }} {{ userInfo.last_name }}</span>
                  <v-btn class="white--text text-capitalize mx-2"
                        small
                        rounded
                        color="blue"
                        @click="follow()">
                    Follow
                  </v-btn>
                  <v-btn class="white--text text-capitalize"
                        small
                        rounded
                        outlined
                        color="blue"
                        @click="logout()">
                    Unfollow
                  </v-btn>
                </div>
                  <span class="subtitle-2 pl-4" align="left">Followers: 0</span>
                  <span class="subtitle-2 pl-4" align="left">Following: {{ userInfo.following.length }}</span>
              </div>
            </v-card-title>

            <v-divider class="mt-1 mb-3"></v-divider>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    v-for="post in userPosts"
                    :key="post.id"
                    class="d-flex child-flex"
                    cols="4">
                    <div>
                      {{ post.description }}
                    <v-img
                      :src="post.picture"
                      :lazy-src="post.picture"
                      aspect-ratio="1"
                      class="grey lighten-2"
                      @click="postDetails(post)">
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center">
                          <v-progress-circular
                            indeterminate
                            color="grey lighten-5"
                          ></v-progress-circular>
                        </v-row>
                      </template>
                    </v-img>
                    </div>
                    <!-- <div>
                    <v-textarea
                      style="position: absolute"
                      class="mx-2"
                      label="Comment"
                      rows="1"
                      prepend-icon="mdi-comment"
                    ></v-textarea>
                    </div> -->
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-card>

          <ViewPostDialog :showDialog="showPostDetails"
                          :postDetails="allPostDetails"
                          :user="currentUser"
                         @cancelClicked="showPostDetails = false"
                         @saveClicked="showPostDetails = false"/>

        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
import ViewPostDialog from '../components/ViewPostDialog'
export default {
  name: 'UserProfile',
  components: {
    ViewPostDialog
  },
  data: () => ({
      loading: false,
      userPosts: {},
      user: null,
      userInfo: null,
      showPostDetails: false,
      allPostDetails: {}
  }),
  methods: {
    follow() {
      // this.loading = true;
      // axios.get('http://localhost:8000/api-auth/user/getAll').then(response => {
      //   this.allUsers = response.data
      //   console.log(this.allUsers)
      //   this.snackbarApproved = true
      // }).catch(e => {
      //   this.snackbarError = true
      //   this.loading = false
      //   console.log(e)
      // })
    },
    fetchPosts() {
      this.showPostDialog = false
      axios.get('http://localhost:8000/content/post/user/' + this.user).then(response => {
         this.userPosts = response.data
         console.log(this.userPosts)
       }).catch(e => {
         console.log(e)
       })
    },
    postDetails(post) {
      console.log(post)
      this.allPostDetails = post
      this.showPostDetails = true
    },
    loadUser(){
      this.userInfo = this.$route.query.userprofile
      this.user = this.userInfo.username
      console.log(this.userInfo)
    }
  },
  mounted() {
    this.loadUser()
    this.fetchPosts()
  },
}
</script>
