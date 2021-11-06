<template>
  <div class="app-container">
    <el-row :gutter="20">
      <el-col :span="20" :xs="24">
        <el-form :inline="true" label-position="right" :model="selectForm">
          <el-form-item size="small" label="项目">
            <el-select
              placeholder="全部"
              v-model="selectForm.project"
              @change="onChangeSubmit"
            >
              <el-option label="全部" />
              <el-option
                v-for="item in projectList"
                :key="item.project_id"
                :label="item.project_name"
                :value="item.project_id"
              />
            </el-select>
          </el-form-item>

          <el-form-item size="small" label="状态">
            <el-select
              placeholder="全部"
              v-model="selectForm.status"
              @change="onChangeSubmit"
            >
              <el-option label="全部" />
              <el-option value="0" label="运行中" />
              <el-option value="1" label="已完成" />
            </el-select>
          </el-form-item>

          <el-button
            type="success"
            icon="el-icon-plus"
            size="small"
            @click="createTaskVisible = true"
            >创建任务</el-button
          >
        </el-form>
      </el-col>
    </el-row>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="taskList"
      border
      aria-setsize
      fit
      highlight-current-row
      style="width: 100%"
    >
      <el-table-column align="center" label="任务ID" width="340">
        <template slot-scope="{ row }">
          <span>{{ row.task_id }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="任务名称" width="250">
        <template slot-scope="{ row }">
          <span>{{ row.task_name }}</span>
        </template>
      </el-table-column>
      <!-- <el-table-column width="70px" align="center" label="等级">
        <template slot-scope="{ row }">
          <span>{{ row.task_level }}</span>
        </template>
      </el-table-column> -->

      <el-table-column width="230px" align="center" label="任务简介">
        <template slot-scope="{ row }">
          <span>{{ row.task_desc }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="" label="运行状态" width="140" align="center">
        <template slot-scope="scope">
          <div>
            <el-button
              v-if="scope.row.task_status == '1'"
              style="font-weight: bold"
              type="primary"
              size="mini"
              plain
              ><i
                class="el-icon-check"
              ></i>
              已完成</el-button
            >
            <el-button
              v-else
              type="success"
              plain
              size="mini"
              ><i
                class="el-icon-loading"
              ></i>
              运行中</el-button
            >
          </div>
        </template>
      </el-table-column>

      <el-table-column prop="" label="上次运行状态" width="140" align="center">
        <template slot-scope="scope">
          <div>
            <el-button
              v-if="scope.row.last_run_status == '1'"
              style="font-weight: bold"
              type="success"
              plain
              ><i
                style="font-weight: bold"
                size="mini"
                class="el-icon-check"
              ></i>
              成功</el-button
            >
            <el-button
              v-else-if="scope.row.last_run_status == '-1'"
              style="font-weight: bold"
              type="danger"
              plain
              size="mini"
              ><i
                style="font-weight: bold"
                size="mini"
                class="el-icon-close"
              ></i>
              失败</el-button
            >
            <el-button
              v-else
              style="font-weight: bold"
              type="primary"
              plain
              size="mini"
              ><i
                style="font-weight: bold"
                size="mini"
                class="el-icon-warning-outline"
              ></i>
              未知</el-button
            >
          </div>
        </template>
      </el-table-column>

      <el-table-column width="200px" align="center" label="上次运行时间">
        <template slot-scope="{ row }">
          <span>{{ row.last_run_time }}</span>
        </template>
      </el-table-column>

      <el-table-column width="200px" align="center" label="创建时间">
        <template slot-scope="{ row }">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" width="360">
        <template slot-scope="{ row, $index }">
          <div>
            <el-tooltip
              class="item"
              effect="dark"
              content="任务详情"
              placement="top-start"
            >
              <el-button
                type="success"
                icon=" el-icon-document"
                size="mini"
                @click="taskDetail(row.task_id)"
                >详情</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="部署"
              placement="top-start"
            >
              <el-button
                type=""
                icon="el-icon-upload"
                size="mini"
                @click="deployTask(row.task_id)"
                >部署</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="查看日志"
              placement="top-start"
            >
              <el-button
                type="primary"
                icon="el-icon-search"
                size="mini"
                @click="onTaskLog(scope.row.taskId)"
                >日志</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="删除"
              placement="top-start"
            >
              <el-button
                type="danger"
                icon="el-icon-delete"
                size="mini"
                @click="deleteTask(row.task_id)"
                >删除</el-button
              >
            </el-tooltip>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total > 0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getTaskList"
    />

    <el-dialog title="添加任务" :visible.sync="createTaskVisible" width="40%">
      <el-form
        rules="rules"
        :model="ruleForm"
        ref="ruleForm"
        label-width="80px"
      >
        <el-form-item prop="" label="任务名称">
          <el-input
            v-model="ruleForm.taskName"
            placeholder="任务名称"
          ></el-input>
        </el-form-item>
        <el-form-item prop="" label="所属项目">
          <el-select v-model="ruleForm.projectId" placeholder="请选择">
            <el-option
              v-for="project in projectList"
              :key="project.project_id"
              :label="project.project_name"
              :value="project.project_id"
              :disabled="project.disabled"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="" label="频率等级">
          <el-select v-model="ruleForm.taskLevel" placeholder="请选择">
            <el-option label="高频" value="高频"></el-option>
            <el-option label="中频" value="中频"></el-option>
            <el-option label="低频" value="低频"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="" label="描述">
          <el-input v-model="ruleForm.taskDesc" placeholder="描述"></el-input>
        </el-form-item>

        <el-form-item prop="" label="上传代码">
          <el-upload
            drag
            http-request=""
            :limit="listQuery.limit"
            before-upload="beforeUpload"
            multiple
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将文件拖到此处，或<em>点击上传</em>
            </div>
            <div class="el-upload__tip" slot="tip">
              只能上传 zip 压缩包，且不超过 10 M
            </div>
          </el-upload>
        </el-form-item>
      </el-form>

      <span slot="footer">
        <el-button @click="createTaskVisible = false">取 消</el-button>
        <el-button type="primary" @click="createTask('ruleForm')"
          >确 定</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
import {
  get_project_list,
  get_task_list,
  create_task,
  delete_task,
} from "@/api/spider";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
  inject: ["reload"],
  name: "SpiderTask",
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      taskList: null,
      projectList: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        project: "",
        status: "",
      },

      selectForm: {
        project: "",
        status: "",
      },

      cityOptions: ["纽约", "巴黎", "北京"],
      createTaskVisible: false,
      dialogStatus: "",

      ruleForm: {
        taskName: "",
        projectId: "",
        taskLevel: "",
        taskDesc: "",
        taskPath: "",
      },
      downloadLoading: false,
    };
  },
  created() {
    this.getTaskList();
    this.getProjectList();
  },
  methods: {
    getTaskList() {
      this.listLoading = true;
      console.log("listQuery: ", this.listQuery);
      get_task_list(this.listQuery).then((response) => {
        console.log("response: ", response);
        this.taskList = response.data.data;
        this.total = response.data.total;
        setTimeout(() => {
          this.listLoading = false;
        }, 1.5 * 1000);
      });
    },
    getProjectList() {
      this.listLoading = true;
      get_project_list({}).then((response) => {
        console.log("response: ", response);
        this.projectList = response.data;
        // this.total = response.data.total;
        setTimeout(() => {
          this.listLoading = false;
        }, 1.5 * 1000);
      });
    },

    createTask(formName) {
      const self = this;
      self.$refs[formName].validate((valid) => {
        if (valid) {
          var data = self.ruleForm;
          create_task(data).then((res) => {
            console.log(res);
            if (res.code === 20000) {
              self.$message.success("创建成功");
              self.reload();
            }
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },

    onChangeSubmit() {
      get_task_list({
        project: this.selectForm.project,
        status: this.selectForm.status,
      }).then((res) => {
        this.taskList = res.data.data;
        this.total = res.data.total;
      });
    },

    deleteTask(taskId) {
      const self = this;
      var data = {
        taskId,
      };
      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          // delete_task(data).then((res) => {
            // if (res.code === 20000) {
              self.$message.error("演示环境 看看得了");
              // self.reload();
            // }
          // });
        })
        .catch(() => {});
    },

    taskDetail(taskId) {
      const self = this;
      self.$router.push(`/task_detail/${taskId}`);
    },

    deployTask(taskId) {
      const self = this;
      self.$router.push(`/task_deploy/${taskId}`);
    },
  },
};
</script>
