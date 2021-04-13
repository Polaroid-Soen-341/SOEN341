<template>
  <div class="text-center">
    <v-dialog
      v-model="showDialog"
      persistent
      width="800">
      <v-card>
        <v-card-title class="headline white--text blue mb-4">
         Post Details
         <v-btn style="position: absolute; right: 6px; top: 16px"
                small
                icon
                color="white"
                @click="cancelClicked()">
                <v-icon>mdi-window-close</v-icon>
          </v-btn>
        </v-card-title>

        <v-card-text>
          <div>
            <v-img
              :src="postDetails.picture"
              :lazy-src="postDetails.picture"
              aspect-ratio="1"
              class="grey lighten-2 mx-4 mb-4">
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
            <div class="px-4">
              <v-btn icon
                      :color="likeBtn? 'pink' : ''"
                      large
                      @click="likeClicked()">
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon
                      color="black"
                      large>
                <v-icon>mdi-comment-outline</v-icon>
              </v-btn>
            </div>
            <div class="px-4">
              20 Likes
            </div>
            <div class="px-4 pb-2">
              <strong>{{ user }}</strong> - {{ postDetails.description }}
            </div>
            <div class="px-4">
              <v-textarea
                label="Add comment..."
                auto-grow
                v-model="postDetails.content"
                filled
                rounded
                rows="1"
                row-height="15"
                append-icon="mdi-send"
                @click:append="sendComment(postDetails.content, postDetails)"
              ></v-textarea>
            </div>
            <div v-for="comment in postDetails.comments"
                  :key="comment.id"
                  class="px-4">
                  <strong>{{ user }}</strong> - {{ comment.content }}
            </div>
          </div>
        </v-card-text>

      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ViewPostDialog',
  props: ['showDialog', 'postDetails', 'user'],
  data () {
    return {
      loading: false,
      newPost: {},
      image: null,
      description: '',
      rules: [
      value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
    ]
    }
  },
  methods: {
    saveClicked() {
      this.loading = true;
      console.log(this.newPost)
      var formData = new FormData()
      formData.append("picture", this.image, this.image.name)
      formData.append("description", this.description)
      console.log(formData.getAll("image"))
      var token = this.$session.get('token')
      axios.post('http://localhost:8000/content/post/', formData, {headers: {Authorization: 'JWT ' + token, 'content-type': 'multipart/form-data'}}).then(response => {
        console.log(response.data)
        }).catch(e => {
        this.loading = false
        console.log(e)
        })
      this.description = ''
      this.image = null
      this.$emit('saveClicked')
    },
    cancelClicked() {
      this.description = ''
      this.image = null
      this.newPost = {}
      this.$emit('cancelClicked')
    }
  }
}
</script>