/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  playbookSelector,
  setErrors,
} from "../../../store/features/playbook/playbookSlice.ts";
import OptionRender from "./OptionRender.jsx";
import VariablesBox from "./VariablesBox.jsx";
import { InfoOutlined } from "@mui/icons-material";
import useCurrentStep from "../../../hooks/useCurrentStep.ts";
import { constructBuilder } from "../../../utils/playbooksData.ts";
import { deepEqual } from "../../../utils/deepEqual.ts";

function TaskDetails({ index }) {
  const data = constructBuilder(index);
  const [step, currentStepIndex] = useCurrentStep(index);
  const dispatch = useDispatch();
  const prevError = useRef(null);
  const { view } = useSelector(playbookSelector);

  const setDefaultErrors = () => {
    const errors = {};
    for (let buildStep of data?.builder) {
      for (let value of buildStep) {
        if (value.isOptional) continue;
        if (!value.key || value.selected) {
          break;
        }
        if (!step[value.key]) {
          errors[value.key] = {
            message: "Please enter a value",
          };
        }
      }
    }

    prevError.current = errors;
    dispatch(setErrors({ errors, index: currentStepIndex }));
  };

  const removeErrors = (key) => {
    const errors = structuredClone(step.errors ?? {});
    delete errors[key];

    prevError.current = errors;
    dispatch(setErrors({ errors, index: currentStepIndex }));
  };

  useEffect(() => {
    const errorChanged = deepEqual(prevError.current, step.errors);
    if (
      !step.isPrefetched &&
      step &&
      data?.builder &&
      Object.keys(step?.errors ?? {}).length === 0 &&
      !errorChanged
    ) {
      setDefaultErrors();
    }
  }, [step]);

  useEffect(() => {
    if (step && data.builder) {
      setDefaultErrors();
    }
  }, [step.taskType, step.source]);

  return (
    <div className="relative mt-2">
      {data?.builder?.map((step, index) => (
        <div
          key={index}
          className={`flex gap-2 flex-wrap ${
            view === "builder" ? "flex-col" : "flex-row"
          }`}>
          {step.map((value, index) =>
            value.condition ?? true ? (
              <div
                key={index}
                style={{
                  display: "flex",
                  flexDirection: view === "builder" ? "column" : "row",
                  gap: "10px",
                  alignItems: "flex-start",
                  flexWrap: "wrap",
                  width: "100%",
                  justifyContent: "flex-start",
                  maxWidth: view === "builder" ? "600px" : "",
                }}>
                <OptionRender
                  data={value}
                  removeErrors={removeErrors}
                  index={currentStepIndex}
                />
              </div>
            ) : (
              <></>
            ),
          )}
        </div>
      ))}
      {step.message && (
        <div className="flex gap-1 items-center my-2 bg-gray-100 rounded p-2 text-sm text-blue-500">
          <InfoOutlined fontSize="small" />
          {step.message}
        </div>
      )}
      <VariablesBox />
    </div>
  );
}

export default TaskDetails;
