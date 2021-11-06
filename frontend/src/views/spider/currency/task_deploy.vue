<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="任务名称" style="font-size: 20px">
        <el-col>{{ detail.task_name }} ({{ detail.task_id }})</el-col>
      </el-form-item>

      <el-form-item label="批量部署">
        <el-checkbox-group v-model="form.hosts">
          <el-checkbox
            v-for="(item, index) in hostList"
            :key="index"
            :label="item.ip"
            @change="handleCheckedHostChange"
            >{{ item.ip }}</el-checkbox
          >
        </el-checkbox-group>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onDeploySubmit">确认部署</el-button>
      </el-form-item>
    </el-form>

    <el-button icon="el-icon-warning" type="" size="samil" class="update-time">
      警告: 该操作将会从主节点中的项目上传至从机的
      <b>{{ detail.task_path }}</b>
      目录
    </el-button>

    <div>
      <el-button type="text" disabled>已部署的节点</el-button>
      <el-button
        type="success"
        plain
        v-for="(item, index) in detail.deployedHosts"
        :key="index"
        >{{ item }}</el-button
      >
    </div>
  </div>
</template>

<style>
.update-time {
  font-size: 14px;
  position: absolute;
  left: 60%;
  top: 80px;
}
.desc {
  color: rgb(97, 94, 94);
  font-size: 12px;
}
</style>
<script>
import { task_detail, deploy_task } from "@/api/spider";
import { host_list } from "@/api/host";
export default {
  name: "SpiderD",
  data() {
    return {
      hostList: [],
      detail: {},
      form: {
        taskId: "",
        hosts: [],
      },
    };
  },

  created() {
    this.form.taskId = this.$route.params.taskId;
    console.log(this.form.taskId);
    this.loadDetail();
    this.loadHostList();
  },
  methods: {
    onDeploySubmit() {
      var data = this.form;
      console.log(data);
      this.$message.success("演示环境，就当部署成功");
      // deploy_task(data).then((res) => {
      // this.$message.success(res.data.message);
      // });
    },

    loadDetail() {
      task_detail({
        taskId: this.form.taskId,
      }).then((res) => {
        this.detail = res.data;
      });
    },

    loadHostList() {
      host_list().then((res) => {
        this.hostList = res.data.items;
      });
    },
  },
};
</script>