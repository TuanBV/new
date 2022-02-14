<template>
  <div class="container-md mt-5">
    <div class="row justify-content-center">
      <div class="col-10">
            <form class="needs-validation">
                <h4 class="title pb-3">Update Profile User</h4>
                <div class="row">
                    <div class="col-3">
                        <label for="fullname" class="form-label">Full Name</label>
                    </div>
                    <div class="col-9">
                        <input type="text" class="form-control" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="username" class="form-label">Username
                            <span class="">(Required)</span>
                        </label>
                    </div>
                    <div class="col-9">
                        <input type="text" class="form-control"  />
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="email" class="form-label">Email 
                            <span class="" >(Required)</span>
                        </label>
                    </div>
                    <div class="col-9">
                        <input type="email" class="form-control" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="Age" class="form-label">Birthday
                            <span class="text-muted"></span>
                        </label>
                    </div>
                    <div class="col-9">
                        <input type="date" class="form-control w-50" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="address" class="form-label">Address</label>
                    </div>
                    <div class="col-9">
                        <input type="text" class="form-control" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="position" class="form-label">Position
                            <span class="" >(Required)</span>
                        </label>
                    </div>
                    <div class="col-9">
                    <table class="col-12">
                        <tr>
                        <td>
                            <label for="rdoPosition3" class="me-2">Member</label>
                            <input type="radio" name="rdoPosition" id="rdoPosition3" value="3" />
                        </td>
                        <td>  
                            <label for="rdoPosition2" class="me-2">Manager</label>
                            <input type="radio" name="rdoPosition" id="rdoPosition2" value="2"/>
                        </td>
                        </tr>
                    </table>
                    </div>
                </div>
                <hr class="my-4" />
                <button type="button" class="btn btn-primary mt-3 w-25" >Update User</button>
                <router-link to="/admin"><button type="button" class="btn btn-danger mt-3 ms-3 w-25">Back</button></router-link>
            </form>
       </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "edit-user",
};
</script>
<style scoped>
.row{
  margin-top: 20px;
}
.col-3{
  text-align: left;
}
span {
  color: red;
}
</style>
