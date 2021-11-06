<template>
  <div class="app-container">
    <div>
      <el-card style="border-radius: 0">
        <div>
          <span class="cpu">
            <el-tag type="success">
              {{ hostDetail.host_name }} ({{ hostDetail.desc }}) 
            </el-tag>

            <el-divider></el-divider>

            <el-tag type="" disabled>运行 {{ hostDetail.info }}</el-tag>
            <el-divider></el-divider>

            <el-tag type="warning">
              {{ hostDetail.pyInfo }}
            </el-tag>
            <el-tag type="danger">
              {{ hostDetail.pipInfo }}
            </el-tag>
          </span>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import { host_detail } from "@/api/host";

export default {
  inject: ["reload"],

  data() {
    return {
      hostDetail: "",
      currentPage: 1, //初始页
      pagesize: 15, // 每页的数据
      activeNames: ["1"],
      rsaPrivateKey:
        "ssh-rsa AAAABwXkmrKsIFfmmFBce2EB7TvOoa/4GCJ1/EajtnP hp@DESKTOP-J85G6E5",
    };
  },

  created() {
    this.handleDetail();
  },

  methods: {
    handleDetail() {
      host_detail({
        uuid: this.$route.params.uuid,
      }).then((res) => {
        this.hostDetail = res.data;
        console.log(res);
      });
    },
  },
};
</script>
 
 
 

 <style>
.install {
  margin-top: 20px;
}
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}

.pagination-footer .description {
  float: left;
  margin-left: 20px;
  margin-top: 12px;
}
.pagination-footer .el-pagination {
  float: right;
  margin-top: 8px;
  margin-bottom: 8px;
}

.cpu {
  white-space: pre-line;
}
</style>
