<template>
  <div class="app-container">
    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="taskList"
      border
      fit
      highlight-current-row
      style="width: 100%"
    >
      <el-table-column align="center" label="任务ID" width="260">
        <template slot-scope="{ row }">
          <span>{{ row.task_id }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="任务名称" width="220">
        <template slot-scope="{ row }">
          <span>{{ row.task_name }}</span>
        </template>
      </el-table-column>
      <el-table-column width="55px" align="center" label="等 级">
        <template slot-scope="{ row }">
          <span>{{ row.task_level }}</span>
        </template>
      </el-table-column>

      <el-table-column width="280px" align="center" label="任务简介">
        <template slot-scope="{ row }">
          <span>{{ row.task_desc }}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="taskStatus"
        label="运行状态"
        width="140"
        align="center"
      >
        <template slot-scope="scope">
          <div>
            <el-button
              v-if="scope.row.task_status == '1'"
              style="font-weight: bold"
              type="primary"
              plain
              ><i
                style="font-weight: bold"
                size="mini"
                class="el-icon-check"
              ></i>
              已完成</el-button
            >
            <el-button
              v-else
              style="font-weight: bold"
              type="success"
              plain
              size="mini"
              ><i
                style="font-weight: bold"
                size="mini"
                class="el-icon-loading"
              ></i>
              运行中</el-button
            >
          </div>
        </template>
      </el-table-column>

      <el-table-column
        prop="lastRunStatus"
        label="上次运行状态"
        width="140"
        align="center"
      >
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

      <el-table-column width="160x" align="center" label="上次运行时间">
        <template slot-scope="{ row }">
          <span>{{ row.last_run_time }}</span>
        </template>
      </el-table-column>

      <el-table-column width="160px" align="center" label="创建时间">
        <template slot-scope="{ row }">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" width="255">
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
                @click="taskDetail(row.task_id)"
              ></el-button>
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="部署"
              placement="top-start"
            >
              <el-button
                type="warning"
                icon="el-icon-upload"
                @click="deployTask(row.task_id)"
              ></el-button>
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
                @click="onTaskLog(scope.row.taskId)"
              ></el-button>
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
                @click="deleteTask(scope.row.taskId)"
              ></el-button>
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
      @pagination="getList"
    />

    <el-dialog title="添加任务" :visible.sync="createTaskVisible" width="40%">
      <el-form
        rules="rules"
        :model="ruleForm"
        ref="ruleForm"
        label-width="80px"
      >
        <el-form-item prop="taskName" label="任务名称">
          <el-input
            v-model="ruleForm.taskName"
            placeholder="任务名称"
          ></el-input>
        </el-form-item>
        <el-form-item prop="projectId" label="所属项目">
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
        <el-form-item prop="taskLevel" label="频率等级">
          <el-select v-model="ruleForm.taskLevel" placeholder="请选择">
            <el-option label="高频" value="高频"></el-option>
            <el-option label="中频" value="中频"></el-option>
            <el-option label="低频" value="低频"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="taskDesc" label="描述">
          <el-input v-model="ruleForm.taskDesc" placeholder="描述"></el-input>
        </el-form-item>

        <el-form-item prop="taskPath" label="上传代码">
          <el-upload
            drag
            http-request="uploadZip"
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
import { get_project_list, task_list, create_task } from "@/api/spider";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
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
        title: "",
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
        // title: [
        //   { required: true, message: "title is required", trigger: "blur" },
        // ],
      },
      downloadLoading: false,
    };
  },
  //   watch: {
  //     $route() {
  //       this.platId = this.$route.params.projectId;
  //       this.projectId = this.$route.params.projectId;
  //     },
  //   },
  created() {
    this.projectId = this.$route.params.projectId;
    this.getList();
    this.getProjectList();
  },
  methods: {
    getList() {
      this.listLoading = true;

      task_list({ projectId: this.projectId }).then((response) => {
        console.log("response: ", response);
        this.taskList = response.data;
        // this.total = response.data.total;
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
    handleFilter() {
      this.listQuery.page = 1;
      this.getList();
    },

    createTask(formName) {
      const self = this;
      self.$refs[formName].validate((valid) => {
        if (valid) {
          var data = self.ruleForm;
          create_task(data).then((res) => {
            if (res.data.code === 200) {
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

    // onChangeSubmit() {
    //   taskIndex({
    //     project: this.selectForm.project,
    //     status:this.selectForm.status
    //   }).then((res) => {
    //     this.taskList = res.data.data;
    //   });
    // },

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
