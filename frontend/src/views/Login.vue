<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md6>
          <v-card class="login-card mt-16">
            <v-card-title class="white--text pl-4" style="background-color: #512DA8">
              <span class="text-h5 headline">Polaroid</span>
            </v-card-title>

            <v-spacer/>

            <v-card-text>

              <v-layout
                row
                fill-height
                justify-center
                align-center
                v-if="loading">
                  <v-progress-circular
                    :size="50"
                    color="primary"
                    indeterminate/>
              </v-layout>


              <v-form v-else ref="form" v-model="valid" lazy-validation>
                <v-container>

                  <v-text-field
                    v-model="credentials.username"
                    :counter="25"
                    label="Username"
                    maxlength="25"
                    required
                    outlined
                    :rules="rules.username"/>

                  <v-text-field
                    type="password"
                    v-model="credentials.password"
                    :counter="20"
                    label="Password"
                    maxlength="20"
                    required
                    outlined
                    :rules="rules.password"/>

                </v-container>
                <v-btn class="white--text" color="deep-purple darken-2" block small :disabled="!valid" @click="login()">Login</v-btn>
                <v-divider class="mt-3 mb-1 mx-3"></v-divider>
                <div class="text-center"> - or - </div>
                <v-divider class="mt-1 mb-3 mx-3"></v-divider>
                <v-btn class="white--text" color="rgb(225 48 108)" block small @click="register()">Register</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
          <v-snackbar v-model="snackbar"
                      :timeout="timeout"
                      absolute
                      bottom
                      color="red">
                      {{ errorMessage }}
          </v-snackbar>

        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Login',
    data: () => ({
        credentials: {},
        valid: true,
        loading: false,
        snackbar: false,
        errorMessage: 'Wrong username or password!',
        timeout: 5000,
        rules: {
          username: [
            v => !!v || 'Username is required',
            v => (v && v.length > 3) || 'A username must be more than 3 characters long',
            v => /^[a-z0-9_]+$/.test(v) || 'A username can only contain letters and digits'
          ],
          password: [
            v => !!v || 'Password is required',
            v => (v && v.length > 7) || 'The password must be longer than 7 characters'
          ]
        }
    }),
    methods: {
        login() {
          if (this.$refs.form.validate()) {
            this.loading = true;
            axios.post('http://localhost:8000/auth/', this.credentials).then(response => {
              this.$session.start();
              this.$session.set('token', response.data.token);
              this.$router.push('/feed');
            }).catch(e => {
              this.snackbar = true
              this.loading = false
              console.log(e)
            })
          }
        },
        register() {
          this.$router.push('/register')
        }
    }
}
</script>
<style>
.instaColor {
  background-color: rgb(225 48 108);
}
</style>
