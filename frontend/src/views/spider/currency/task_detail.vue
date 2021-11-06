<template>
  <div class="app-container">
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item
          label="爬虫名称"
          style="font-size: 20px"
        >
          <el-col>{{ detail.task_name }} ({{ detail.task_id }})</el-col>
        </el-form-item>

        <el-button icon="el-icon-time" type="" size="samil" class="update-time">
          <time class="time">{{ detail.last_run_time }}</time>
        </el-button>

        <el-form-item
          label="执行命令"
          style="font-weight: bold; font-size: 20px"
        >
          <el-input
            v-model="form.cmd"
            style="width: 200px"
            clearable
            placeholder="请输入 cmd"
          ></el-input>
        </el-form-item>

        <el-form-item label="选择节点">
          <el-checkbox-group
            v-model="form.hosts"
            v-if="detail.deployed_host.length > 0"
          >
            <el-checkbox
              v-for="(item, index) in detail.deployed_host"
              :key="index"
              :label="item"
              @change="handleCheckedHostChange"
              >{{ item }}</el-checkbox
            >
          </el-checkbox-group>
          <el-link v-else type="warning" :underline="false"
            >还没部署节点?
          </el-link>
        </el-form-item>
        <!-- <el-form-item
            label="Cookie"
            style="font-weight: bold; font-size: 20px"
          >
            <el-input type="textarea" rows="5" v-model="form.cookie"></el-input>
          </el-form-item>-->
        <el-form-item>
          <el-button type="primary" @click="onSubmit">运行</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>


<style>
.update-time {
  font-size: 14px;
  position: absolute;
  left: 80%;
  top: 80px;
}
.desc {
  color: rgb(97, 94, 94);
  font-size: 12px;
}
</style>

<script>
import { task_detail, start_task } from "@/api/spider";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination
export default {
  name: "SpiderDetail",
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      form: {
        taskId: "",
        hosts: [],
        cmd: "",
        // date: "",
        // date_time: "",
        // delivery: true,
        // cookie: "",
        // bing: 60,
      },
      cmd: "输入cmd命令",
      detail: {},
      hostList: [],
    };
  },
  created() {
    this.form.taskId = this.$route.params.taskId;
    this.loadDetail();
    // this.loadHostList();
  },
  methods: {
    loadDetail() {
      task_detail({
        taskId: this.form.taskId,
      }).then((res) => {
        this.detail = res.data;
      });
    },
    onSubmit() {
      var data = this.form;
      console.log(data);
      this.$message.success("抓取中");
      // start_task(data).then((res) => {
        // if (res.data.code === 200) {
          this.$notify({
            title: "成功",
            message:
              // res.data.data.taskName +
              " 更新成功 " +
              new Date().toLocaleTimeString(),
            type: "success",
            duration: 0,
          });
        // } else {
        //   this.$message.error(res.data);
        // }
      // });
    },

    // loadHostList() {
    //   host_list().then((res) => {
    //     this.hostList = res.data.data;
    //   });
    // },

    handleCheckedHostChange() {
      console.log(this.form.host);
    },
  },
};
</script>

