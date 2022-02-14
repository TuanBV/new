var schema = {
  type: "object",
  properties: {
    nameTime: {
      type: "string",
      minLength: 1,
      maxLength: 200,
    },
    timeStart: { 
      type: "date"
    },
    timeEnd: { 
      type: "date", 
    },
  },
  additionalProperties: false,
};
export default schema

