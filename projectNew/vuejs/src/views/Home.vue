<template>
  <div class="home">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-xl-8 mx-auto">
                <div class="my-4">
                    <form>
                        <div class="row mt-3 align-items-center">
                            <div class="col-6 text-center mb-5">
                                <div class="avatar avatar-xl">
                                    <img src="../assets/image.png" alt="..." class="avatar-img rounded-circle" />
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-row">
                                    <div class="form-group">
                                        <label for="lastname">Fullname</label>
                                        <input type="text" id="fullname" class="form-control" v-model="fullname" placeholder="Bui Tuan" readonly/>
                                    </div>
                                </div>
                                <div class="form-group mt-2">
                                    <label for="inputEmail4">Email</label>
                                    <input type="email" class="form-control" id="email"
                                        placeholder="brown@asher.me" v-model="email" readonly/>
                                </div>
                                <div class="form-group mt-2">
                                    <label for="inputAddress5">Address</label>
                                    <input type="text" class="form-control" id="address"
                                        placeholder="P.O. Box 464, 5975 Eget Avenue" v-model="address" readonly/>
                                </div>
                                <div class="form-row mt-2">
                                    <div class="form-group col-md-6">
                                        <label for="inputCompany5">Birthday</label>
                                        <input type="date" class="form-control" id="birthday"
                                            placeholder="" v-model="birthday" readonly/>
                                    </div>
                                    <div class="form-group col-md-4 mt-2">
                                        <label for="inputState5">Position</label>
                                        <input type="text" class="form-control" id="position"
                                            placeholder="Admin" v-model="position" readonly/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    setup() {
        const obj = JSON.parse(localStorage.getItem('user'))[0];
        var fullname = obj.fullname;
        var email = obj.email;
        var address = obj.address;
        var birthday = obj.birthday;
        var position = obj.name;
        return {
            fullname,
            email,
            address,
            birthday,
            position
        }
    },
}
</script>

<style scoped>
.form-group{
    text-align: left;
}

</style>
