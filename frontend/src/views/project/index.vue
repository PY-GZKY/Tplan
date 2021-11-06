<template>
  <div class="app-container">
    <div class="elcol">
      <el-button
        type="success"
        icon="el-icon-plus"
        size="mini"
        @click="createProVisible = true"
        >新建项目</el-button
      >
    </div>

    <el-row :gutter="8">
      <el-col
        class="elcol"
        :span="8"
        :xs="24"
        v-for="(o, i_index) in projectList"
        :key="i_index"
        :offset="0"
      >
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>{{ o.project_name }} ({{ o.project_id }})</span>
          </div>
          <div style="height: 150px">
            <el-form>
              <el-form-item>
                {{ o.project_desc }}
              </el-form-item>
              <el-form-item>
                <span>
                  {{ o.update_time }}
                </span>
              </el-form-item>
            </el-form>

            <div slot="footer" class="dialog-footer">
              <el-button
                type="success"
                icon="el-icon-edit"
                size="mini"
                @click="goTaskList(o.project_id)"
                >查看</el-button
              >
              <el-button
                type="danger"
                icon="el-icon-delete"
                size="mini"
                @click="deleteProject(o.project_id)"
                >删除</el-button
              >
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 编辑弹出框 -->
    <el-dialog title="添加项目" :visible.sync="createProVisible" width="40%">
      <el-form ref="form" :model="createForm" label-width="80px">
        <el-form-item label="项目名称">
          <el-input
            v-model="createForm.projectName"
            placeholder="项目名称"
          ></el-input>
        </el-form-item>
        <el-form-item label="项目简介">
          <el-input
            v-model="createForm.projectDesc"
            placeholder="项目简介"
          ></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer">
        <el-button @click="createProVisible = false">取 消</el-button>
        <el-button type="primary" @click="createProject">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<style>
.elcol {
  margin-top: 10px;
  /* margin-left: 1px; */
}

.update-time {
  font-size: 14px;
  margin-top: 8px;
  margin-left: 12px;
}

.desc {
  font-size: 13px;
  color: rgb(97, 96, 96);
}

.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 19px;
}

.button {
  padding: 5px;
  float: right;
  font-weight: bold;
}

.button-red {
  padding: 5px;
  float: right;
  color: #ff0000;
  font-weight: bold;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>

<script>
import { get_project_list, create_project, delete_project } from "@/api/spider";

export default {
  inject: ["reload"],
  data() {
    return {
      projectList: [],
      projectId: "",
      title: "",
      createProVisible: false,
      createForm: {
        projectName: "",
        porjectDesc: "",
      },
      currentDate: new Date(),
    };
  },

  watch: {
    $route() {
      this.projectId = this.$route.params.projectId;
    },
  },

  created() {
    this.loadProjectIndex();
  },

  methods: {
    loadProjectIndex() {
      const self = this;
      get_project_list().then((res) => {
        console.log(res);
        self.projectList = res.data;
      });
    },
    // 跳转到爬虫列表详情
    goTaskList(projectId) {
      const self = this;
      self.$router.push(`/proj/${projectId}`);

      // self.$router.push({
      //   path: "spiderPro",
      //   query: {
      //     projectId: projectId,
      //   },
      // });
    },

    deleteProject(projectId) {
      var self = this;
      var data = {
        projectId,
      };
      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          self.$message.success("你一定点错了");
          self.reload();
          // delete_project(data).then((res) => {
          //   if (res.data.code === 200) {
          //     self.$message.success("删除成功");
          //     self.reload();
          //   }
          // });
        })
        .catch(() => {});
    },

    createProject() {
      var self = this;
      var data = this.createForm;
      create_project(data).then((res) => {
        self.$message.success({
          dangerouslyUseHTMLString: true,
          message: "创建成功",
        });
        self.reload();
      });
    },
  },
};
</script>