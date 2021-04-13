<template>
    <v-container grid-list-sm>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm12 lg12 md12>
          <v-card class="mx-12 mt-2">
            <v-card-title class="black--text pl-4">
              <v-avatar
                color="blue"
                size="100">
                <span class="white--text">{{ currentUser }}</span>
              </v-avatar>
              <div>
                <div class="pb-2">
                  <span class="text-h5 headline px-4" align="left">{{ currentUser }}</span>
                </div>
                  <span class="subtitle-2 pl-4" align="left">Followers: 0</span>
                  <span class="subtitle-2 pl-4" align="left">Following: 0</span>
              </div>
            </v-card-title>

            <v-divider class="mt-1 mb-3"></v-divider>

            <v-card-text>
              <div class="px-3 pb-2 mt-n2" align="right">
                <v-btn class="white--text text-capitalize"
                       color="blue"
                       rounded
                       @click="newPost()">
                  <v-icon left>
                    mdi-plus
                  </v-icon>
                  New Post
                </v-btn>
              </div>
              <v-container>
                <v-row>
                  <v-col
                    v-for="post in myPosts"
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

          <NewPostDialog :showDialog="showPostDialog"
                         @cancelClicked="showPostDialog = false"
                         @saveClicked="fetchPosts()"/>
          
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
import NewPostDialog from '../components/NewPostDialog'
import ViewPostDialog from '../components/ViewPostDialog'
import axios from 'axios';
export default {
  name: 'MyProfile',
  components: {
    NewPostDialog,
    ViewPostDialog
  },
  data: () => ({
    currentUser: '',
    myPosts: {},
    loading: false,
    showPostDialog: false,
    showPostDetails: false,
    allPostDetails: {}
  }),
  methods: {
    newPost() {
      this.showPostDialog = true
    },
    postDetails(post) {
      console.log(post)
      this.allPostDetails = post
      this.showPostDetails = true
    },
    fetchPosts() {
      this.showPostDialog = false
      axios.get('http://localhost:8000/content/post/user/' + this.currentUser).then(response => {
         this.myPosts = response.data
         console.log(this.myPosts)
       }).catch(e => {
         console.log(e)
       })
    },
    loadUser(){
      this.currentUser = this.$session.get('current_user')
    }
  },
  mounted() {
    this.loadUser()
    this.fetchPosts()
  },
}
</script>
