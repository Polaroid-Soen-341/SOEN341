<template>
  <div class="text-center">
    <v-dialog
      v-model="showDialog"
      persistent
      width="800">
      <v-card>
        <v-card-title class="headline white--text blue">
          New Post
        </v-card-title>

        <v-file-input v-model="image"
                      :rules="rules"
                      class="px-8"
                      accept="image/png, image/jpeg, image/bmp"
                      prepend-icon="mdi-camera"
                      label="Picture"/>
        <v-textarea v-model="description"
                    class="px-8"
                    prepend-inner-icon="mdi-comment"
                    counter
                    outlined
                    name="input-7-4"
                    label="Description"
        ></v-textarea>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="white--text text-capitalize"
            color="blue"
            @click="saveClicked()">
            Post
          </v-btn>
          <v-btn
            class="white--text text-capitalize"
            outlined
            color="blue"
            @click="cancelClicked()">
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'PostDialog',
  props: ['showDialog'],
  data () {
    return {
      loading: false,
      newPost: {},
      image: null,
      description: '',
      rules: [
      value => !value || value.size < 2000000 || 'Image size should be less than 2 MB!',
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